from flask import Flask, render_template, request, jsonify
from text_to_speech import text_to_speech

print("Starting to set up Flask application...")

app = Flask(__name__)

print("Flask app created")

@app.route('/')
def index():
    print("Index route accessed")
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    print("Speak route accessed")
    text= request.form['text']
    language= request.form['language']
    text_to_speech(text, language)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    print("About to run the Flask app")
    app.run(debug=True)
    print("Flask app has finished running")