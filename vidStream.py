from flask import Flask,render_template,Response
from time import sleep
import cv2

app = Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template("./video_stream.html")

def read_video():
    cap = cv2.VideoCapture(0)
    while True:
        
        success, frame = cap.read()
        if success:
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            sleep(0.1)
        else:
            break


@app.route('/video_feed')
def Video_Feed():
    return Response(read_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port = 5123)
    