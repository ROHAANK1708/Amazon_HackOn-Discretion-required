import pandas as pd
import numpy as np

# Define payment methods and their characteristics
payment_methods = ['UPI', 'Credit Card', 'Debit Card', 'Amazon Pay Balance', 'Amazon Pay Later',
                   'Net Banking', 'Easy Monthly Installments (EMI)', 'Pay on Delivery']

# Generate mock data
np.random.seed(42)  # for reproducibility

# Create 10,000 customer IDs
customer_ids = np.arange(1, 10001)

# Randomly sample payment methods and generate attributes
data = {
    'customer_id': np.random.choice(customer_ids, 10000),
    'payment_method': np.random.choice(payment_methods, 10000),
    'success_rate': np.round(np.random.uniform(0.8, 1.0, 10000), 2),  # Random success rate between 0.8 and 1.0
    'cashback_offered': np.random.randint(0, 10, 10000),  # Random cashback offered (scaled from 0 to 10)
    'transaction_fee': np.round(np.random.uniform(0.1, 2.0, 10000), 2),  # Random transaction fee
    'customer_preference': np.random.randint(0, 11, 10000)  # Customer preference score (scaled from 0 to 10)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('mock_dataset.csv', index=False, encoding='utf-8')

print("Mock dataset with 10,000 entries created and saved as 'mock_dataset.csv'.")
