import tensorflow as tf
import pandas as pd
from transformers import BertTokenizer, TFBertForSequenceClassification
from transformers import glue_convert_examples_to_features
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import TensorBoard

# Load the data and perform basic EDA
data = pd.read_csv('Resume\Resume.csv')

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data['Resume_str'], data['Category'], test_size=0.2, random_state=42)

# Load a pretrained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(data['Category'].unique()))

# Preprocess the data for BERT
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train_encoded))
test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test_encoded))

def convert_to_transformer_features(text, label):
    return text, label

train_dataset = train_dataset.map(convert_to_transformer_features)
test_dataset = test_dataset.map(convert_to_transformer_features)

# Tokenize the training and testing data
train_encodings = tokenizer(list(X_train), truncation=True, padding=True, max_length=128)
test_encodings = tokenizer(list(X_test), truncation=True, padding=True, max_length=128)

# Convert the tokenized data into a tf.data.Dataset format
train_dataset = tf.data.Dataset.from_tensor_slices((
    dict(train_encodings),
    y_train_encoded
)).shuffle(100).batch(32).repeat(2)

test_dataset = tf.data.Dataset.from_tensor_slices((
    dict(test_encodings),
    y_test_encoded
)).batch(64)

# Batch the dataset
train_dataset = train_dataset.shuffle(100).batch(32).repeat(2)
test_dataset = test_dataset.batch(64)

# Fine-tune the BERT model on the training data
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=3e-5, epsilon=1e-08, clipnorm=1.0),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=[tf.keras.metrics.SparseCategoricalAccuracy('accuracy')])

# Use TensorBoard for visualization
tensorboard_callback = TensorBoard(log_dir='./logs')

model.fit(train_dataset, epochs=2, validation_data=test_dataset, callbacks=[tensorboard_callback])