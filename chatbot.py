from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(_name_)
CORS(app)

payment_queries = {
    "What is my payment status?": "Your payment is being processed.",
    "How do I make a payment?": "You can make a payment through our website or by contacting our customer support team.",
    "Can I get a refund?": "Please contact our customer support team to request a refund.",
    "What payment methods do you accept?": "We accept credit cards, debit cards, and PayPal.",
    "Can I pay in installments?": "Yes, you can choose our installment plan at checkout.",
    "How do I update my payment information?": "You can update your payment information in your account settings.",
    "What is the currency used for payments?": "All payments are processed in USD.",
    "Can I change my billing address?": "Yes, you can update your billing address in your account settings.",
    "Is there a late payment fee?": "Yes, a late fee will be applied if your payment is overdue.",
    "How do I cancel a payment?": "Please contact our customer support team to cancel a payment.",
    "Why was my payment declined?": "Your payment may have been declined due to insufficient funds or incorrect payment details.",
    "How do I get a payment receipt?": "A receipt will be sent to your registered email after the payment is processed.",
    "Can I pay with a different currency?": "Currently, we only accept payments in USD.",
    "What is the payment processing time?": "Payments are usually processed within 1-2 business days.",
    "Can I save my payment information for future use?": "Yes, you can save your payment information in your account settings.",
    "Is my payment information secure?": "Yes, we use industry-standard encryption to protect your payment information.",
    "How do I check my payment history?": "You can view your payment history in your account settings.",
    "Can I pay over the phone?": "Yes, you can make a payment by contacting our customer support team.",
    "How do I set up automatic payments?": "You can enable automatic payments in your account settings.",
    "What if I overpay?": "Any overpayment will be credited to your account or refunded upon request.",
    "Do you offer discounts for early payments?": "Currently, we do not offer discounts for early payments.",
    "What happens if I miss a payment?": "A late fee may be applied, and your service may be interrupted.",
    "Can I use multiple payment methods?": "No, you can only use one payment method per transaction.",
    "How do I apply a promo code?": "You can enter your promo code at checkout to apply the discount.",
    "Can I pay with a check?": "Currently, we do not accept check payments.",
    "Do you have a mobile payment option?": "Yes, you can make payments using our mobile app.",
    "What is your refund policy?": "Please refer to our refund policy on the website for more details.",
    "Can I prepay for services?": "Yes, you can prepay for services during the checkout process.",
    "How do I resolve a payment dispute?": "Please contact our customer support team to resolve any payment disputes.",
    "What are the accepted card types?": "We accept Visa, MasterCard, American Express, and Discover cards.",
    "How do I request an invoice?": "You can request an invoice by contacting our customer support team.",
}

def handle_payment_query(query):
    return payment_queries.get(query, "I don't know. Please ask a different question.")

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/payment_query', methods=['POST'])
def payment_query():
    data = request.get_json()
    query = data.get('query', '')
    response = handle_payment_query(query)
    return jsonify({'response': response})

if _name_ == '_main_':
    app.run(debug=True)
