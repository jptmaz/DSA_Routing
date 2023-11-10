from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)


@app.route('/areaOfcirle', methods=['GET', 'POST'])
def calculate_area():
    result = None
    if request.method == 'POST':
        radius = request.form.get('radius', '')
        try:
            radius = float(radius)
            area = 3.14159 * (radius ** 2)
            result = round(area, 2)
        except ValueError:
            result = "Invalid input. Please enter a valid number."

    return render_template('circle_area.html', result=result)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def area_of_triangle():
    result = None
    if request.method == 'POST':
        base = request.form.get('base', '')
        height = request.form.get('height', '')
        try:
            base = float(base)
            height = float(height)
            area = 0.5 * base * height
            result = f"{area:.2f}"  # Format the result to two decimal places.
        except ValueError:
            result = "Invalid input. Please enter valid numbers for the base and height."

    return render_template('areaOfTriangle.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
