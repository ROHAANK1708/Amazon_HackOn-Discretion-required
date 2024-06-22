# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler, LabelEncoder
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# # Load your dataset (mock dataset in this case)
# df = pd.read_csv('mock_dataset.csv')

# # Display the first few rows to understand the dataset structure
# print(df.head())

# # Define categorical and numerical features
# categorical_features = ['payment_method']
# numerical_features = ['success_rate', 'cashback_offered', 'transaction_fee', 'customer_preference']

# # Encode categorical features
# label_encoders = {}
# for feature in categorical_features:
#     le = LabelEncoder()
#     df[feature] = le.fit_transform(df[feature])
#     label_encoders[feature] = le

# # Separate features and target variable
# X = df.drop(columns=['customer_id', 'payment_method'])
# y = df['payment_method']

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Standardize numerical features
# scaler = StandardScaler()
# X_train[numerical_features] = scaler.fit_transform(X_train[numerical_features])
# X_test[numerical_features] = scaler.transform(X_test[numerical_features])

# # Train a Random Forest classifier
# clf = RandomForestClassifier(random_state=42)
# clf.fit(X_train, y_train)

# # Predict on the test set
# y_pred = clf.predict(X_test)

# # Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy}")

# # Example of predicting with new data
# new_data = pd.DataFrame({
#     'success_rate': [0.85, 0.92],
#     'cashback_offered': [3, 4],
#     'transaction_fee': [1.2, 0.8],
#     'customer_preference': [5, 8]
# })

# # Ensure categorical features are in the correct format
# for feature in categorical_features:
#     if feature in new_data.columns:
#         new_data[feature] = label_encoders[feature].transform(new_data[feature])

# # Standardize numerical features in new_data
# new_data[numerical_features] = scaler.transform(new_data[numerical_features])

# # Predict the payment method for new_data
# predictions = clf.predict(new_data)
# print(f"Predictions for new_data: {predictions}")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load your dataset (mock dataset in this case)
df = pd.read_csv('mock_dataset.csv')

# Display the first few rows to understand the dataset structure
print(df.head())

# Define categorical and numerical features
categorical_features = ['payment_method']
numerical_features = ['success_rate', 'cashback_offered', 'transaction_fee', 'customer_preference']

# Encode categorical features
label_encoders = {}
for feature in categorical_features:
    le = LabelEncoder()
    df[feature] = le.fit_transform(df[feature])
    label_encoders[feature] = le

# Separate features and target variable
X = df.drop(columns=['customer_id', 'payment_method'])
y = df['payment_method']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize numerical features
scaler = StandardScaler()
X_train[numerical_features] = scaler.fit_transform(X_train[numerical_features])
X_test[numerical_features] = scaler.transform(X_test[numerical_features])

# Train a Random Forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Example of predicting with new data
new_data = pd.DataFrame({
    'success_rate': [0.85, 0.92],
    'cashback_offered': [3, 4],
    'transaction_fee': [1.2, 0.8],
    'customer_preference': [5, 8]
})

# Ensure categorical features are in the correct format
for feature in categorical_features:
    if feature in new_data.columns:
        new_data[feature] = label_encoders[feature].transform(new_data[feature])

# Standardize numerical features in new_data
new_data[numerical_features] = scaler.transform(new_data[numerical_features])

# Predict the payment method for new_data
predictions = clf.predict(new_data)

# Decode the predicted labels back to payment method names
predicted_methods = label_encoders['payment_method'].inverse_transform(predictions)
print(f"Predicted payment methods for new_data: {predicted_methods}")
