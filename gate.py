from flask import Flask, request, jsonify
import requests as req
import generator as gen
import time
import datetime

app = Flask(__name__)

host = "https://api.gateio.ws"
prefix = "/api/v4"
common_headers = {"Accept": "application/json", "Content-Type": "application/json"}

@app.route("/spot/orders", methods=["GET"])  # U can change the url 'like spot-orders' and call url = '/spot/orders' inside the methode
def get_open_orders():

    url = str(request.url_rule)
    # url = '/spot/orders'

    # Get query parameters
    currency_pair = request.args.get("currency_pair")
    status = request.args.get("status")

    # Log the parameters (optional, for debugging)
    query_param = f"currency_pair={currency_pair}&status={status}"

    sign_headers = gen.gate_sign("GET", prefix + url, query_param)
    common_headers.update(sign_headers)
    r = req.request(
        "GET", host + prefix + url + "?" + query_param, headers=common_headers
    )

    # Simulated open orders data
    orders = r.json()

    # Filter orders based on query parameters
    filtered_orders = [
        order
        for order in orders
        if order["currency_pair"] == currency_pair and order["status"] == status
    ]

    return jsonify(filtered_orders) 


@app.route("/spot-trades", methods=["GET"])
def get_trades():
    
    # url = str(request.url_rule)
    url = '/spot/my_trades'

    # Define the 'from' and 'to' query parameters
    # from_timestamp = 1710499900  # time in seconds
    # to_timestamp = 1712999900
    # to_timestamp = int(time.time() * 1000)  # Current time in milliseconds

    # The date string
    # Get query parameters
    from_date_string = request.args.get("from")  # "2024-02-25"
    to_date_string = request.args.get("to")  # "2024-03-24"

    # Convert the date string to a datetime object
    from_date = datetime.datetime.strptime(from_date_string, "%Y-%m-%d")
    to_date = datetime.datetime.strptime(to_date_string, "%Y-%m-%d")
    print(f"from {from_date} to {to_date}")

    # current_date = datetime.date.today()
    # Convert the current date to a datetime object (with the time set to midnight)
    from_datetime = datetime.datetime.combine(from_date, datetime.datetime.min.time())
    to_datetime = datetime.datetime.combine(to_date, datetime.datetime.min.time())

    # Convert the datetime object to a timestamp
    from_timestamp = int(time.mktime(from_datetime.timetuple()))
    to_timestamp = int(time.mktime(to_datetime.timetuple()))

    # current_datetime_utc = datetime.datetime.now(datetime.timezone.utc)
    # print(current_datetime_utc)
    # timestamp = current_datetime_utc.timestamp()

    print(f"{from_timestamp} to {to_timestamp}")

    # Construct the query string
    query_param = f"from={from_timestamp}&to={to_timestamp}"

    # query_param = 'currency_pair=BOME_USDT'
    # for `gen_sign` implementation, refer to section `Authentication` above
    sign_headers = gen.gate_sign("GET", prefix + url, query_param)
    common_headers.update(sign_headers)
    r = req.request(
        "GET", host + prefix + url + "?" + query_param, headers=common_headers
    )

    # Simulated open trades data
    trades = r.json()

    return jsonify(trades)


if __name__ == "__main__":
    app.run(debug=True)
