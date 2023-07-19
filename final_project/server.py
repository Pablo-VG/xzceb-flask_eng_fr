from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    """Translate from English to French"""
    textToTranslate = request.args.get('textToTranslate')
    return translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    """Translate from French to English"""
    textToTranslate = request.args.get('textToTranslate')
    return translator.french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    """Render index.html"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
