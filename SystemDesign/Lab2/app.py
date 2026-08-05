import cv2
import numpy as np
from flask import Flask, Response, request

app = Flask(__name__)


@app.post("/gray")
def gray():
    file = request.files["image"]
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, out = cv2.imencode(".jpg", gray)
    return Response(out.tobytes(), mimetype="image/jpeg")


@app.post("/blur")
def blur():
    file = request.files["image"]
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    blur = cv2.GaussianBlur(img, (15, 15), 0)

    _, out = cv2.imencode(".jpg", blur)
    return Response(out.tobytes(), mimetype="image/jpeg")


@app.post("/edges")
def edges():
    file = request.files["image"]
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    _, out = cv2.imencode(".jpg", edges)
    return Response(out.tobytes(), mimetype="image/jpeg")


@app.post("/contours")
def contours():
    file = request.files["image"]
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, cnts, -1, (0, 255, 0), 2)

    _, out = cv2.imencode(".jpg", img)
    return Response(out.tobytes(), mimetype="image/jpeg")


app.run(host="0.0.0.0", port=3229)
