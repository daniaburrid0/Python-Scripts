from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    event_reports = []

    if request.method == 'POST':
        api_key = request.form['api_key']
        response = requests.get(f'https://api.nasa.gov/DONKI/notifications?api_key={api_key}&type=all')

        if response.status_code == 200:
            event_reports = response.json()

    return render_template('index.html', event_reports=event_reports)

if __name__ == '__main__':
    app.run(debug=True)
