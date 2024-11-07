from flask import Flask, render_template, request
from model import get_apod
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    apod_data = get_apod(today)
    return render_template('index.html', apod=apod_data)

@app.route('/history', methods=['GET', 'POST'])
def history():
    apod_data = None
    if request.method == 'POST':
        date = request.form['date']
        apod_data = get_apod(date)
    return render_template('history.html', apod=apod_data)

if __name__ == '__main__':
    app.run(debug = True)