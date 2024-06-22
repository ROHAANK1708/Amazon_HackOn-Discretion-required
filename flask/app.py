from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf

# Load your trained model
model = tf.keras.models.load_model('D:\Amazon_HackOn-Discretion-required\MODEL\payment_method_model.h5')

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    success_rate = float(data['success_rate'])
    cashback_offered = int(data['cashback_offered'])
    transaction_fee = float(data['transaction_fee'])
    customer_preference = int(data['customer_preference'])
    
    # Prepare input features for prediction
    input_data = np.array([[success_rate, cashback_offered, transaction_fee, customer_preference]])
    
    # Predict using the model
    prediction = model.predict(input_data)
    
    # Assuming the model directly outputs the name of the best payment method
    recommended_payment_method = prediction[0]
    
    # Return the recommended payment method
    return jsonify({'recommended': recommended_payment_method})

if __name__ == '__main__':
    app.run(debug=True)
