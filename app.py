from flask import Flask, render_template, jsonify, request
import random
import json

app = Flask(__name__)

def load_json_data():
    with open('words.json', 'r') as file:
        return json.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_words/<set_number>', methods=['GET'])
def get_words(set_number):
    data = load_json_data()
    words = data['words'].get(f'Set{set_number}', [])
    selected_words = random.sample(words, 25) if len(words) >= 25 else words
    return jsonify(selected_words)

@app.route('/get_clue/<set_number>', methods=['GET'])
def get_clue(set_number):
    data = load_json_data()
    clues = data['clues'].get(f'Set{set_number}', [])
    return jsonify(clues)

@app.route('/get_ai_hint/<set_number>', methods=['GET'])
def get_ai_hint(set_number):
    data = load_json_data()
    ai_hints = data['AI'].get(f'Set{set_number}', {})
    return jsonify(ai_hints)

@app.route('/submit_selected_words', methods=['POST'])
def submit_selected_words():
    selected_words = request.json.get('words')
    print(selected_words)  # 打印接收到的单词列表
    return jsonify({"status": "success", "words": selected_words})


if __name__ == '__main__':
    app.run(debug=True)
