#!/bin/sh


# Run the Python script to generate the HTML file
python --version

cd ./app

python generate.html
# Start Nginx
nginx -g 'daemon off;'


