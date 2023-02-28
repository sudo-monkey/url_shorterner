from flask import Flask, request, redirect, Response
import hashlib
import requests
from urllib.parse import urlparse

app = Flask(__name__)

# Path to the file that stores URL mappings
URL_MAP_FILE = 'url_map.txt'

def load_url_map():
    # Load the URL mappings from the file
    url_map = {}

    with open(URL_MAP_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                unique_id, original_url = line.split('\t')
                url_map[unique_id] = original_url

    return url_map

def save_url_map(url_map):
    # Save the URL mappings to the file
    with open(URL_MAP_FILE, 'w') as f:
        for unique_id, original_url in url_map.items():
            f.write(f'{unique_id}\t{original_url}\n')

# Load the URL mappings from the file at startup
url_map = load_url_map()

@app.route('/', methods=['POST'])
def shorten_url():
    # Get the original URL from the request body
    original_url = request.form.get('url')

    # Validate the original URL
    if not is_valid_url(original_url):
        return 'Invalid URL', 400

    # Generate a unique ID for the URL
    unique_id = hashlib.sha256(original_url.encode()).hexdigest()[:8]

    # Create the unique URL by appending the ID to the host name
    unique_url = f'http://{request.host}/{unique_id}'

    # Store the URL mapping in the file
    url_map[unique_id] = original_url
    save_url_map(url_map)

    # Return the unique URL to the user
    return unique_url

@app.route('/<unique_id>', methods=['GET'])
def redirect_url(unique_id):
    # Look up the original URL for the given unique ID
    original_url = url_map.get(unique_id)

    # If the URL is found, redirect the user to it or return its contents
    if original_url:
        # Make a GET request to the original URL
        response = requests.get(original_url)

        # If the response status code is 200, return its contents
        if response.status_code == 200:
            return Response(response.content, mimetype=response.headers['Content-Type'])

        # Otherwise, redirect the user to the original URL
        return redirect(original_url)

    # If the URL is not found, return a 404 error
    return 'URL not found', 404

def is_valid_url(url):
    # Parse the URL and check if it has a scheme and a netloc
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme and parsed_url.netloc)

if __name__ == '__main__':
    app.run()
