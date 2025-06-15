from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    salary = int(request.form['salary'])
    taxable_income = max(0, salary - 1448000 - 430000)
    income_tax = 0
    if taxable_income <= 1950000:
        income_tax = taxable_income * 0.05
    elif taxable_income <= 3300000:
        income_tax = taxable_income * 0.10 - 97500
    # Add more brackets as needed

    return f"Estimated Income Tax: ¥{round(income_tax)}"