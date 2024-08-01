from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
CORS(app, resources={r"/add": {"origins": "*"}})

def translate(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def translate_text():
    data = request.get_json()
    x = data.get('x')
    y = data.get('languageSelect')

    
    if y in LANGUAGES:
        output = translate(x, y)
        return jsonify(output=output)
    else:
        return jsonify(error="Invalid language code")

if __name__ == "__main__":
    app.run(debug=True)