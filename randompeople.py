import random
import string
from flask import Flask, jsonify

app = Flask(__name__)

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_email():
    username = generate_random_string(8)
    domain = generate_random_string(5)
    return f"{username}@{domain}.com"

def generate_random_person():
    age = random.randint(18, 65)
    city = generate_random_string(10)
    country = generate_random_string(10)
    first_name = generate_random_string(6)
    last_name = generate_random_string(8)
    email = generate_random_email()
    return {
        "age": age,
        "city": city,
        "country": country,
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }

@app.route('/random_person', methods=['GET'])
def get_random_person():
    person = generate_random_person()
    return jsonify(person)

if __name__ == '__main__':
    app.run()
