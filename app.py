from flask import Flask
from flask import render_template

app = Flask (__name__)

@app.route("/fizzbuzz")
def fizzbuzz():
    """Loop through number 1 -100 inside of an unordered list """
    numbers = list(range(1, 101))
    fizzbuzz_list = []
    for number in numbers:
        if number % 3 == 0 and number % 5 == 0:
            fizzbuzz_list.append("FizzBuzz")
        elif number % 3 == 0:
            fizzbuzz_list.append("Fizz")
        elif number % 5 == 0:
            fizzbuzz_list.append("Buzz")
        else:
            fizzbuzz_list.append(str(number))
    return render_template("fizzbuzz.html", fizzbuzz_list=fizzbuzz_list)