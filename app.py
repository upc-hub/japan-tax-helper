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

# New route for the combined tax explanations page
@app.route('/tax-explanations')
def tax_explanations():
    return render_template('tax_explanations.html')

if __name__ == '__main__':
    app.run(debug=True)