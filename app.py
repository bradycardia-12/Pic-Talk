
from flask import Response, send_from_directory
from flask import Flask, render_template, request, send_file
from pytesseract import pytesseract
from werkzeug.utils import secure_filename
import numpy as np
from keras.preprocessing import image
from flask import Flask, request, render_template
from PIL import Image


from gtts import gTTS
import os
from langdetect import detect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def upload():
    return render_template('index.html')

@app.route('/predict2', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        max_length = 32
        pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        extractedInformation = pytesseract.image_to_string(Image.open(file_path),
                                                           lang="eng+fra+ita+deu+spa+por+nld")
        Text_generated = extractedInformation
        return Text_generated
    return None

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/predict', methods=['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        max_length = 32
        pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        extractedInformation = pytesseract.image_to_string(Image.open(file_path),
                                                           lang="eng+fra+ita+deu+spa+por+nld")
        Text_generated = extractedInformation
        language = detect(Text_generated)
        text = Text_generated
        speech = gTTS(text=text, lang=language, slow=False)
        speech.save("static/text2.mp3")
        return send_file(
            "static/text2.mp3",
            mimetype="audio/mpeg",
            as_attachment=True,
            attachment_filename="text2.mp3")
    return None


if __name__ == '__main__':
    app.run(debug=True)
