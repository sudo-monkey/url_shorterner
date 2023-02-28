#!/bin/bash

# Set the URL to be shortened
url='https://www.google.com/'

# Send a POST request to the Flask app to shorten the URL
shortened_url=$(curl -s -X POST -d "url=$url" http://localhost:5000/)

# Remove the quotes from the shortened URL
shortened_url=${shortened_url//\"}

# Send a GET request to the Flask app using the shortened URL
http_status=$(curl -s -w "%{http_code}" $shortened_url -o /dev/null)

# Check if the HTTP status code is 200
if [ $http_status -eq 200 ]; then
    echo "Successful request: $shortened_url"
else
    echo "Failed request: $shortened_url"
fi
