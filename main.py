from flask import Flask,request
from flask import render_template
from fer import FER
import cv2
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template("hello.html")
    else:
        img = request.files['imagefile']
        img_path = "./static/user_image/"+img.filename
        img.save(img_path)
        try:
            image = cv2.imread(img_path)
            det = FER()
            rs = det.detect_emotions(image)
            return render_template(("result.html"), rs=rs)
        except:
            return "Something went wrong"



app.run(debug=False,host='0.0.0.0')
