from flask import Flask, request
import random

app = Flask(__name__)
@app.route('/random', methods=['POST'])
def generate_random():
    power = int(request.json['power'])
    turns = int(request.json['turns']) # each turn is * 24 hours in a cycle
    
    if power < 0 or power > 210:
        return 'Invalid input'

    min_max = (50 - power, 250 + power)
    element = ['ice', 'platinum', 'nickel','regolith', 'silicate'] # replace with your own list of valid elements
    
    number = random.randint(min_max[0], min_max[1])
    rand_element = str(random.choice(list(element)))

    response = {
        'element': rand_element,
        'number': number,
        'message': f'{rand_element} with a random number between {min_max[0]} and {min_max[1]}'
    }

    return response
if __name__ == '__main__':
    app.run(debug=True)