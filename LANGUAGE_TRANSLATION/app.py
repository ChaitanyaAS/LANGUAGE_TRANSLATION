from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    translation = ''
    if request.method == 'POST':
        # Get text input and target language from the form
        lang_1 = request.form['text_input']
        target_lang = request.form['target_language']
        
        if lang_1 == '':
            translation = "Please enter text to translate!"
        else:
            # Create Translator instance and translate text
            translator = Translator()
            try:
                translated = translator.translate(lang_1, dest=target_lang)
                translation = translated.text
            except Exception as e:
                translation = f"Error: {str(e)}"
    
    # Render the HTML page with translation result
    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
