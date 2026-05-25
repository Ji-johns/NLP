from googletrans import Translator

def translate_text():
    translator = Translator()
    text = 'My name is Ajin and i study in 3rd year enginnering'
    to_lang = 'ja'

    result = translator.translate(text, src='en', dest=to_lang)
    print("Translated Text:", result.text)

# Run the function
translate_text()
