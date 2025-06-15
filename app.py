from flask import Flask, render_template

app = Flask(__name__)

# Route for the main homepage with cards
@app.route('/')
def home():
    return render_template('home.html')

# Route for the Resident Tax Calculator (your existing tool)
@app.route('/resident-tax-calculator')
def resident_tax_calculator():
    return render_template('resident_tax_calculator.html')

# Route for the Income Tax Calculator (new page)
@app.route('/income-tax-calculator')
def income_tax_calculator():
    # For now, this directs to a placeholder page.
    # You can later build the full calculator logic here.
    return render_template('income_tax_calculator.html')

# Route for the Resident Tax Explanation
@app.route('/resident-tax-explanation')
def resident_tax_explanation():
    # We can use a generic explanation template and pass data to it
    tax_type = "Resident Tax (住民税)"
    explanation_details = """
    <p>Resident Tax is a local tax levied by your prefecture and municipality based on your previous year's income.</p>
    <h4>Key Components:</h4>
    <ul>
        <li><strong>Income-based Portion (所得割):</strong> A flat rate of 10% on your taxable income after all deductions (6% for municipal, 4% for prefectural).</li>
        <li><strong>Per-Capita Portion (均等割):</strong> A small, fixed annual fee. It is typically around ¥5,000.</li>
    </ul>
    <p>It's important to note that you pay this tax in the year *after* you earn the income. For example, tax on your 2024 income is paid starting from June 2025.</p>
    """
    return render_template('tax_explanation.html', title=tax_type, details=explanation_details)

# Route for the Income Tax Explanation
@app.route('/income-tax-explanation')
def income_tax_explanation():
    tax_type = "Income Tax (所得税)"
    explanation_details = """
    <p>National Income Tax is a progressive tax levied by the national government on your current year's income.</p>
    <h4>Key Features:</h4>
    <ul>
        <li><strong>Progressive Rates:</strong> The tax rate increases as your income increases, ranging from 5% to 45%.</li>
        <li><strong>Withholding Tax (源泉徴収):</strong> For salaried employees, this tax is usually estimated and deducted directly from your monthly paycheck by your employer.</li>
        <li><strong>Year-End Adjustment (年末調整):</strong> Your employer typically performs a year-end adjustment to finalize your exact tax liability for the year, accounting for various deductions.</li>
    </ul>
    """
    return render_template('tax_explanation.html', title=tax_type, details=explanation_details)

if __name__ == '__main__':
    app.run(debug=True)