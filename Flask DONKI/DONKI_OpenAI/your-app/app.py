from flask import Flask, render_template, request
import requests
import logging
import json
from dotenv import load_dotenv
import os

# Logging setup
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nasa_api_key = request.form['nasa_api_key']
        openai_api_key = request.form['openai_api_key']
        
        # Fetch data from NASA DONKI API
        donki_data = fetch_donki_data(nasa_api_key)
        
        # Process data with GPT-4
        processed_data = process_with_gpt4(openai_api_key, donki_data)

        return render_template('index.html', processed_data=processed_data)
    
    return render_template('index.html', processed_data=None)

def fetch_donki_data(api_key):
    url = "https://api.nasa.gov/DONKI/notifications?startDate=2023-01-01&endDate=2023-01-30&api_key=" + api_key
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info("Fetched data successfully from NASA DONKI API.")
        return response.json()
    except requests.exceptions.HTTPError as err:
        logging.error(f"HTTP error occurred: {err}")
        return f"Error fetching data from NASA DONKI API: {err}"
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return f"Error fetching data from NASA DONKI API: {e}"

def process_with_gpt4(api_key, document):
    openai_url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    prompt = f"Please analyze the following document and summarize its key points in JSON format: {document}"
    messages = [
        {"role": "system", "content": "Return a summary in JSON format."},
        {"role": "user", "content": prompt}
    ]

    data = {
        "model": "gpt-4-1106-preview",
        "messages": messages,
        "response_format": {"type": "json_object"}
    }

    try:
        response = requests.post(openai_url, headers=headers, json=data)
        response.raise_for_status()
        logging.info("Data processed successfully with GPT-4.")
        response_content = json.loads(response.text)
        return json.dumps(response_content['choices'][0]['message']['content'], indent=4)
    except requests.exceptions.HTTPError as err:
        logging.error(f"HTTP error occurred: {err}")
        return f"Error processing data with GPT-4: {err}"
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return f"Error processing data with GPT-4: {e}"

# Test functions for debugging
def test_fetch_donki_data():
    test_api_key = "your_test_nasa_api_key"
    result = fetch_donki_data(test_api_key)
    logging.info(f"Test fetch DONKI data result: {result}")

def test_process_with_gpt4():
    test_api_key = "your_test_openai_api_key"
    test_document = "Test document content"
    result = process_with_gpt4(test_api_key, test_document)
    logging.info(f"Test process with GPT-4 result: {result}")

if __name__ == '__main__':
    test_fetch_donki_data()  # Test the DONKI data fetch function
    test_process_with_gpt4()  # Test the GPT-4 processing function
    app.run(debug=True)
