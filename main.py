from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/A1G')
def a1g():
    code = """
def pure_function(a, b):
    return a + b
result = pure_function(2, 3)
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-A1G</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-A1G</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/A1F')
def a1f():
    code = """
immutable_value = (1, 2)
result = immutable_value[0] + immutable_value[1]
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-A1F</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-A1F</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/A1E')
def a1e():
    code = """
# Objekt-Orientiert
class Calculator:
    def add(self, a, b):
        return a + b

# Funktional
def add(a, b):
    return a + b

calc = Calculator()
oo_result = calc.add(2, 3)
funk_result = add(2, 3)
result = (oo_result, funk_result)
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-A1E</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-A1E</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/B1G')
def b1g():
    code = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-B1G</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-B1G</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/B1F')
def b1f():
    code = """
def square(n):
    return n * n

def add(a, b):
    return a + b

result = add(square(2), square(3))
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-B1F</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-B1F</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/B1E')
def b1e():
    code = """
def add(a, b):
    return a + b

def apply_operation(a, b, operation):
    return operation(a, b)

result = apply_operation(2, 3, add)
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-B1E</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-B1E</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/B2G')
def b2g():
    code = """
def greet(name):
    return f"Hello, {name}!"

greeting = greet
result = greeting("Alice")
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-B2G</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-B2G</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/B2F')
def b2f():
    code = """
def square(n):
    return n * n

def apply_function(func, value):
    return func(value)

result = apply_function(square, 5)
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-B2F</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-B2F</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/B2E')
def b2e():
    code = """
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
result = double(5)
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-B2E</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-B2E</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/B3G')
def b3g():
    code = """
square = lambda x: x * x
result = square(4)
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-B3G</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-B3G</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/B3F')
def b3f():
    code = """
adder = lambda x, y: x + y
result = adder(3, 7)
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-B3F</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-B3F</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/B3E')
def b3e():
    code = """
names = ['Alice', 'Bob', 'Charlie']
sorted_names = sorted(names, key=lambda x: len(x))
result = sorted_names
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-B3E</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-B3E</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/B4G')
def b4g():
    code = """
from functools import reduce

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))
filtered = list(filter(lambda x: x > 4, squared))
summed = reduce(lambda x, y: x + y, filtered)
result = summed
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-B4G</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-B4G</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/B4F')
def b4f():
    code = """
from functools import reduce

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = list(filter(lambda x: x % 2 == 0, data))
squared = list(map(lambda x: x ** 2, filtered))
result = reduce(lambda x, y: x + y, squared)
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-B4F</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-B4F</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/B4E')
def b4e():
    code = """
from functools import reduce

data = [{'value': 1}, {'value': 2}, {'value': 3}, {'value': 4}, {'value': 5}]
filtered = list(filter(lambda x: x['value'] > 2, data))
values = list(map(lambda x: x['value'], filtered))
result = reduce(lambda x, y: x * y, values)
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-B4E</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-B4E</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)


@app.route('/C1G')
def c1g():
    code = """
    
def calculate_area(radius):
    return 3.14 * radius * radius

area = calculate_area(5)

def calculate_square(number):
    return number * number

square_result = calculate_square(4)

numbers = [1, 2, 3]
total_sum = sum(numbers)

def get_discounted_price(price, discount):
    return price * (1 - discount)

discounted_price = get_discounted_price(100, 0.2)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
rectangle_area = rect.area()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(3, 4)

def live_code():
    return "I am necessary"

live_code_result = live_code()

def is_adult(age):
    return age >= 18

adult_check = is_adult(20)
"""
    exec_globals = {}
    exec(code, exec_globals)
    area = exec_globals['area']
    square_result = exec_globals['square_result']
    total_sum = exec_globals['total_sum']
    discounted_price = exec_globals['discounted_price']
    rectangle_area = exec_globals['rectangle_area']
    live_code_result = exec_globals['live_code_result']
    adult_check = exec_globals['adult_check']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-C1G</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-C1G</h1>
            <pre>{{ code }}</pre>
            <p>Area of Circle: {{ area }}</p>
            <p>Square Result: {{ square_result }}</p>
            <p>Total Sum: {{ total_sum }}</p>
            <p>Discounted Price: {{ discounted_price }}</p>
            <p>Rectangle Area: {{ rectangle_area }}</p>
            <p>Live Code Result: {{ live_code_result }}</p>
            <p>Is Adult Check: {{ adult_check }}</p>
            <a href="/" class="return-button">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, area=area, square_result=square_result, total_sum=total_sum, discounted_price=discounted_price, rectangle_area=rectangle_area, live_code_result=live_code_result, adult_check=adult_check)

@app.route('/C1F')
def c1f():
    code = """
def process_data(data):
    return sum([x * 2 for x in data if x % 2 == 0])

def double_even_sum(data):
    evens = filter(lambda x: x % 2 == 0, data)
    doubled = map(lambda x: x * 2, evens)
    return sum(doubled)

data = [1, 2, 3, 4, 5]
result = double_even_sum(data)
"""
    exec_globals = {}
    exec(code, exec_globals)
    result = exec_globals['result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-C1F</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-C1F</h1>
            <pre>{{ code }}</pre>
            <p>Result: {{ result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, result=result)

@app.route('/C1E')
def c1e():
    code = """
def sum_even_numbers():
    data = [1, 2, 3, 4, 5]
    return sum([x for x in data if x % 2 == 0])

def sum_even(data):
    return sum(x for x in data if x % 2 == 0)

original_result = sum_even_numbers()
refactored_result = sum_even([1, 2, 3, 4, 5])
"""
    exec_globals = {}
    exec(code, exec_globals)
    original_result = exec_globals['original_result']
    refactored_result = exec_globals['refactored_result']
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>M323-C1E</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <div class="content-wrapper">
            <h1>M323-C1E</h1>
            <pre>{{ code }}</pre>
            <p>Original Result: {{ original_result }}</p>
            <p>Refactored Result: {{ refactored_result }}</p>
            <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 15px; color: white; background-color:#000080; text-decoration: none; border-radius: 5px;">Return to Home</a>
        </div>
    </body>
    </html>
    """, code=code, original_result=original_result, refactored_result=refactored_result)



if __name__ == '__main__':
    app.run(debug=True)


