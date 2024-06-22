from flask import Flask, request, render_template, redirect, url_for, flash
import json
from datetime import datetime
from twilio.rest import Client as TwilioClient
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Twilio and SendGrid configuration
TWILIO_SID = 'your_twilio_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
SENDGRID_API_KEY = 'your_sendgrid_api_key'
FROM_EMAIL = 'your_email@example.com'
TO_EMAIL = 'recipient_email@example.com'
TO_PHONE_NUMBER = 'recipient_phone_number'

twilio_client = TwilioClient(TWILIO_SID, TWILIO_AUTH_TOKEN)
sendgrid_client = SendGridAPIClient(SENDGRID_API_KEY)

class BudgetManager:
    def __init__(self, data_file='budget_data.json'):
        self.data_file = data_file
        self.load_data()
        
    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {
                'limits': {},
                'expenses': {},
                'savings': 0,
            }
            
    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)
            
    def set_purchase_limit(self, year, limit):
        self.data['limits'][year] = limit
        self.save_data()
        
    def add_expense(self, amount, category, date=None):
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        year = date.split('-')[0]
        
        if year not in self.data['expenses']:
            self.data['expenses'][year] = {}
        
        if category not in self.data['expenses'][year]:
            self.data['expenses'][year][category] = 0
        
        self.data['expenses'][year][category] += amount
        self.save_data()
        
        self.check_threshold(year)
        
    def get_expense(self, year, category=None):
        if year not in self.data['expenses']:
            return 0
        
        if category:
            return self.data['expenses'][year].get(category, 0)
        
        return sum(self.data['expenses'][year].values())
    
    def track_savings(self):
        for year in self.data['limits']:
            limit = self.data['limits'][year]
            spent = self.get_expense(year)
            self.data['savings'] = limit - spent
        self.save_data()
        
    def check_threshold(self, year):
        limit = self.data['limits'].get(year, 0)
        spent = self.get_expense(year)
        
        if spent > limit * 0.75 and spent <= limit * 0.9:
            self.send_alert(f"Alert: You have spent 75% of your budget for the year {year}.")
        elif spent > limit * 0.9 and spent <= limit:
            self.send_alert(f"Alert: You have spent 90% of your budget for the year {year}.")
        elif spent > limit:
            self.send_alert(f"Alert: You have exceeded your budget for the year {year}.")
        
    def send_alert(self, message):
        # Send SMS
        twilio_client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=TO_PHONE_NUMBER
        )
        # Send Email
        email = Mail(
            from_email=FROM_EMAIL,
            to_emails=TO_EMAIL,
            subject='Budget Alert',
            plain_text_content=message
        )
        sendgrid_client.send(email)
    
    def get_savings(self):
        self.track_savings()
        return self.data['savings']
    
    def get_monthly_expenses(self, year):
        if year not in self.data['expenses']:
            return {}
        
        monthly_expenses = {month: 0 for month in range(1, 13)}
        for category, amount in self.data['expenses'][year].items():
            date = datetime.strptime(category.split('-')[1], '%Y-%m-%d')
            month = date.month
            monthly_expenses[month] += amount
        
        return monthly_expenses
    
    def get_category_expenses(self, year):
        if year not in self.data['expenses']:
            return {}
        
        return self.data['expenses'][year]

budget_manager = BudgetManager()

@app.route('/')
def index():
    return render_template('index.html', limits=budget_manager.data['limits'], savings=budget_manager.get_savings())

@app.route('/set_limit', methods=['POST'])
def set_limit():
    year = request.form['year']
    limit = float(request.form['limit'])
    budget_manager.set_purchase_limit(year, limit)
    flash(f'Purchase limit for {year} set to {limit}', 'success')
    return redirect(url_for('index'))

@app.route('/add_expense', methods=['POST'])
def add_expense():
    amount = float(request.form['amount'])
    category = request.form['category']
    date = request.form['date']
    budget_manager.add_expense(amount, category, date)
    flash(f'Expense of {amount} added to {category} on {date}', 'success')
    return redirect(url_for('index'))

@app.route('/expenses/<year>')
def view_expenses(year):
    monthly_expenses = budget_manager.get_monthly_expenses(year)
    category_expenses = budget_manager.get_category_expenses(year)
    return render_template('expenses.html', year=year, monthly_expenses=monthly_expenses, category_expenses=category_expenses)

if __name__ == '__main__':
    app.run(debug=True)
