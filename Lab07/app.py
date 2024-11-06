from flask import Flask, request, render_template
import segno
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_qr_code():
    qrcode = None
    message = None
    if request.method == 'POST':
        message = request.form['data']
        qrcode = segno.make(message)
        image_path = os.path.join('static','vampire-blues.png')
        qrcode.save(image_path, border =10)
    return render_template('index.html', qrcode=qrcode, message=message)
if __name__ == '__main__':
    app.run(port=18, debug=True)
    