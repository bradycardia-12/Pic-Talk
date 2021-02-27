import os

from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
from gtts import gTTS
import os
from langdetect import detect



app = Flask(__name__)

@app.route('/', methods=['GET'])
def upload():
    return render_template('index.html')

@app.route('/generate', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
          if request.form['btn-text']=='read_text':
            f = request.files['file']
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
            f.save(file_path)
          elif request.form['btn-audio']=='read_audio':
              read_audio()
          else:
              pass


    return None

@app.route('/', methods=['POST'])
def read_audio():
    if request.method == "POST":
        user = request.form["test_temp"]
        Text_generated="hello"
        language = detect(Text_generated)
        text = Text_generated
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("text2.mp3")
        os.system("start text2.mp3")
def read_text():
    pass


if __name__ == '__main__':
    app.run()