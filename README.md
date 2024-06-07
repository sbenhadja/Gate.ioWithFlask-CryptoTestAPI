# Mini Project: Practicing Flask with Gate.io API

# Overview
This mini project aims to practice using Flask with the Gate.io API. The project uses Python 3.11.8 and Flask to retrieve open orders and all trades within a defined period via API requests.

# Features
Retrieve open orders from the Gate.io exchange.
Retrieve all trades within a defined period.
Securely handle API keys and secrets.

# Requirements
    Python 3.11.8
    Flask
    Requests library (for making HTTP requests to the Gate.io API)

# Setup
*Clone the Repository:*

    git clone <repository_url>
    cd <repository_directory>

*Install Dependencies:*
Make sure you have Python 3.11.8 installed. Then, install the necessary Python packages:

    pip install Flask requests
    Create dont_share.py:

Create a file named dont_share.py in the project directory. This file will contain your API key and secret.
# dont_share.py
    API_KEY = 'your_api_key_here'
    API_SECRET = 'your_api_secret_here'

# Run the Flask Application:
*Start the Flask application by running:*

    python app.py

# Usage
The Flask application will be available at http://127.0.0.1:5000.
Use the provided endpoints to get open orders and trades within a defined period.

# Example Endpoints:
*Get Open Orders:*
http://127.0.0.1:5000/spot/orders?currency_pair=BOME_USDT&status=open
This endpoint retrieves the open BOME_USDT orders from your Gate.io account.

*Get Trades in Defined Period:*
http://127.0.0.1:5000/spot-trades?from=2024-02-25&to=2024-03-24
This endpoint retrieves all trades within the specified time period.

# Notes
Ensure that you keep your dont_share.py file secure and do not share it publicly, as it contains sensitive API credentials.
This project is for practicing purposes. For a production environment, consider implementing more robust error handling, logging, and security measures.

# License
This project is licensed under the MIT License.
