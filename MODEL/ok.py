import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load your dataset (mock dataset in this case)
df = pd.read_csv('mock_dataset.csv')

# Define categorical features
categorical_features = ['payment_method']

# Initialize label encoders
label_encoders = {}

# Encode categorical features
for feature in categorical_features:
    le = LabelEncoder()
    df[feature] = le.fit_transform(df[feature])
    label_encoders[feature] = le
    
# Save label encoders
for feature, encoder in label_encoders.items():
    np.save(f'label_encoder_{feature}.npy', encoder.classes_)
    
# Save preprocessed data
df.to_csv('preprocessed_data.csv', index=False)
