import pandas as pd
import numpy as np

# Define the number of entries you want in the dataset
num_entries = 100

# Generate random data for each column
success_rate = np.random.uniform(0.7, 1.0, size=num_entries)
cashback_offered = np.random.randint(1, 6, size=num_entries)
transaction_fee = np.random.uniform(0.5, 2.0, size=num_entries)
customer_preference = np.random.randint(5, 11, size=num_entries)
payment_methods = ['UPI', 'Credit Card', 'Debit Card', 'Amazon Pay Balance', 'Amazon Pay Later',
                   'Net Banking', 'Easy Monthly Installments (EMI)', 'Pay on Delivery']

payment_method = np.random.choice(payment_methods, size=num_entries)

# Create DataFrame
new_data = pd.DataFrame({
    'success_rate': success_rate,
    'cashback_offered': cashback_offered,
    'transaction_fee': transaction_fee,
    'customer_preference': customer_preference,
    'payment_method': payment_method
})

# Save to CSV
new_data.to_csv('new_data.csv', index=False)

print(f"new_data.csv with {num_entries} entries has been created successfully.")
