import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load your test dataset
test_data = pd.read_csv('new_data.csv')

# Define numerical features
numerical_features = ['success_rate', 'cashback_offered', 'transaction_fee', 'customer_preference']

# Load label encoders for categorical features
label_encoders = {}
for feature in ['payment_method']:
    le = LabelEncoder()
    le.classes_ = np.load(f'label_encoder_{feature}.npy', allow_pickle=True)
    label_encoders[feature] = le

# Load the trained model
model = tf.keras.models.load_model('payment_method_model.h5')

# Preprocess the test data
scaler = StandardScaler()
test_data[numerical_features] = scaler.fit_transform(test_data[numerical_features])

# Predict on the preprocessed test data
predictions = model.predict(test_data[numerical_features])

# Map predictions back to payment method names
predicted_payment_methods = label_encoders['payment_method'].inverse_transform(np.argmax(predictions, axis=1))

# Add predicted payment method to test data
test_data['predicted_payment_method'] = predicted_payment_methods

# Print or save the results
print(test_data[['success_rate', 'cashback_offered', 'transaction_fee', 'customer_preference', 'predicted_payment_method']])
