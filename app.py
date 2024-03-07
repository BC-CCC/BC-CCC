from flask import Flask, render_template, jsonify
from fortune_teller import FortuneTeller

app = Flask(__name__)
fortune_teller = FortuneTeller()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cast_coins', methods=['POST'])
def cast_coins():
    results = [fortune_teller.cast_coins() for _ in range(6)]
    interpretations = [fortune_teller.interpret_results(result) for result in results]
    names = [get_result_name(result) for result in results]

    return jsonify({'results': results, 'interpretations': interpretations, 'names': names})

def get_result_name(result):
    heads_count = result.count('Heads')
    tails_count = result.count('Tails')

    if heads_count == 3:
        return 'Old Yang'
    elif tails_count == 3:
        return 'Old Yin'
    elif heads_count == 2:
        return 'Little Yang'
    elif tails_count == 2:
        return 'Little Yin'
    else:
        return 'Unknown'

if __name__ == '__main__':
    app.run(debug=True)