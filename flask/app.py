# from flask import Flask, request, jsonify
# import numpy as np
# import tensorflow as tf

# app = Flask(__name__)

# # Load your model
# model = tf.keras.models.load_model('D:\Amazon_HackOn-Discretion-required\MODEL\payment_method_model.h5')


# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         data = request.get_json()
#         success_rate = data['success_rate']
#         cashback_offered = data['cashback_offered']
#         transaction_fee = data['transaction_fee']
#         customer_preference = data['customer_preference']

#         # Prepare the input for the model
#         input_data = np.array([[success_rate, cashback_offered, transaction_fee, customer_preference]])
        
#         # Make a prediction
#         prediction = model.predict(input_data)
#         recommended_payment_method = prediction[0]

#         # Ensure the output is in a JSON serializable format
#         recommended_payment_method = recommended_payment_method.tolist()

#         return jsonify({'recommended': recommended_payment_method}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Load your model
model = tf.keras.models.load_model('D:\Amazon_HackOn-Discretion-required\MODEL\payment_method_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        success_rate = data['success_rate']
        cashback_offered = data['cashback_offered']
        transaction_fee = data['transaction_fee']
        customer_preference = data['customer_preference']

        # Prepare the input for the model
        input_data = np.array([[success_rate, cashback_offered, transaction_fee, customer_preference]])
        
        # Make a prediction
        prediction = model.predict(input_data)[0]  # Assuming the model returns an array of scores
        payment_methods = ['UPI', 'Credit Card', 'Debit Card', 'Amazon Pay Balance', 'Amazon Pay Later',
                   'Net Banking', 'Easy Monthly Installments (EMI)', 'Pay on Delivery']  # Modify based on your actual methods
        
        # Create a dictionary of payment methods and their scores
        payment_scores = {payment_methods[i]: float(prediction[i]) for i in range(len(payment_methods))}
        
        # Find the recommended payment method
        recommended_payment_method = max(payment_scores, key=payment_scores.get)

        return jsonify({'recommended': recommended_payment_method, 'scores': payment_scores}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
