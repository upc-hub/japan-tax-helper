from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    monthly_salary = int(request.form['salary'])
    annual_salary = monthly_salary * 12

    # Salary income deduction logic (simplified)
    if annual_salary <= 1625000:
        deduction = 550000
    elif annual_salary <= 1800000:
        deduction = annual_salary * 0.4 - 100000
    elif annual_salary <= 3600000:
        deduction = annual_salary * 0.3 + 80000
    elif annual_salary <= 6600000:
        deduction = annual_salary * 0.2 + 440000
    elif annual_salary <= 8500000:
        deduction = annual_salary * 0.1 + 1100000
    else:
        deduction = 1950000

    taxable_income = annual_salary - deduction - 430000  # basic deduction
    taxable_income = max(taxable_income, 0)

    # Income tax (only 5% bracket here for simplicity)
    if taxable_income <= 1950000:
        income_tax = taxable_income * 0.05
    else:
        income_tax = 1950000 * 0.05 + (taxable_income - 1950000) * 0.1  # extend logic as needed

    return f"<h2>Estimated Income Tax: ¥{int(income_tax):,}</h2><a href='/'>← Back</a>"

if __name__ == '__main__':
    app.run(debug=True)