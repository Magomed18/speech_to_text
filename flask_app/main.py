from flask import Flask, render_template, request, redirect
#import speech_recognition as sr
from google.cloud import speech
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/maga/Desktop/py_project/My Project 9820-ff4f6091aa84.json'
app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    text = ''
    

    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        #Processing an audiofile
          
        if file: 
             # recognizer = sr.Recognizer()
             # audioFile = sr.AudioFile(file)
             # with audioFile as source:
             #     data = recognizer.record(source)
             # text = recognizer.recognize_google(data, key=None)

            #Google Speech API
            client = speech.SpeechClient()
            config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=8000,
            language_code="en-US",
            )
            content = request.files['file'].read()
            audio = speech.RecognitionAudio(content=content)
            response = client.recognize(config=config, audio=audio)
            
            for result in response.results:
                text = result.alternatives[0].transcript
                
   
    return render_template('index.html', text=text)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

