from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_url, title, explanation = None, None, None

    if request.method == 'POST':
        api_key = request.form['api_key']
        response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}')
        
        if response.status_code == 200:
            data = response.json()
            image_url = data.get('url')
            title = data.get('title')
            explanation = data.get('explanation')

    return render_template('index.html', image_url=image_url, title=title, explanation=explanation)

if __name__ == '__main__':
    app.run(debug=True)
