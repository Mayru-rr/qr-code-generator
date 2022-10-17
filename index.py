from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/done', methods=['GET', 'POST'])
def done():
    subn = request.form['Subn']
    qr = qrcode.make(subn)
    qr.save("static/mayur.jpg")
    return render_template("done.html")

app.run(debug=True)
