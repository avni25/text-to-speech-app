from flask import Flask, redirect, url_for, render_template, request
from gtts import gTTS
from playsound import playsound
import os
import time

app = Flask(__name__)


    

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        
        a = request.form["txt"]
        tts = gTTS(str(a), tld='co.uk')
        try:
            os.remove("draft.mp3")
        except OSError as e: # name the Exception `e`
            print ("Failed with:"+e.strerror) # look what it says
             
        tts.save("draft.mp3")
        playsound('draft.mp3')
        time.sleep(3)
        os.remove("draft.mp3")
        print("----------------------------------------- ")         
    return render_template("index.html")    



if __name__ == "__main__":
    app.run()
    
    
    


