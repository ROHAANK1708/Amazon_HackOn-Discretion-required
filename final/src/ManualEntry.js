import React, { useState } from 'react';
import axios from 'axios';
import './ManualEntry.css';

const ManualEntry = () => {
  const [formData, setFormData] = useState({
    success_rate: '',
    cashback_offered: '',
    transaction_fee: '',
    customer_preference: ''
  });

  const [recommendedPaymentMethod, setRecommendedPaymentMethod] = useState('');
  const [otherPaymentOptions, setOtherPaymentOptions] = useState([]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Convert values to numbers before sending to Flask
    const dataToSend = {
      success_rate: parseFloat(formData.success_rate),
      cashback_offered: parseFloat(formData.cashback_offered),
      transaction_fee: parseFloat(formData.transaction_fee),
      customer_preference: parseFloat(formData.customer_preference)
    };

    try {
      const response = await axios.post('http://127.0.0.1:5000/predict', dataToSend);
      const { recommended } = response.data;
      setRecommendedPaymentMethod(recommended);
    } catch (error) {
      console.error('Error fetching the recommended payment method:', error);
    }
  };

  return (
    <div className="payment-container">
      <h2 className="section-title">Select a payment method</h2>
      <form onSubmit={handleSubmit} className="payment-form">
        <div className="input-group">
          <label htmlFor="success_rate">Success Rate:</label>
          <input
            type="number"
            name="success_rate"
            id="success_rate"
            value={formData.success_rate}
            onChange={handleChange}
            required
          />
        </div>
        <div className="input-group">
          <label htmlFor="cashback_offered">Cashback Offered:</label>
          <input
            type="number"
            name="cashback_offered"
            id="cashback_offered"
            value={formData.cashback_offered}
            onChange={handleChange}
            required
          />
        </div>
        <div className="input-group">
          <label htmlFor="transaction_fee">Transaction Fee:</label>
          <input
            type="number"
            name="transaction_fee"
            id="transaction_fee"
            value={formData.transaction_fee}
            onChange={handleChange}
            required
          />
        </div>
        <div className="input-group">
          <label htmlFor="customer_preference">Customer Preference:</label>
          <input
            type="number"
            name="customer_preference"
            id="customer_preference"
            value={formData.customer_preference}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" className="submit-button">Get Recommended Payment Method</button>
      </form>

      {recommendedPaymentMethod && (
        <div className="payment-options">
          <h3>Recommended Payment Method</h3>
          <div className="payment-option">
            <input type="radio" id="recommended" name="payment" checked disabled />
            <label htmlFor="recommended">{recommendedPaymentMethod}</label>
          </div>
        </div>
      )}
    </div>
  );
};

export default ManualEntry;
