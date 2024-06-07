from flask import Flask, request
app = Flask(__name__)

@app.route('/hello/<int:id>')#, methods=['GET']) GET is default here
def hello_world(id):
    # Get query parameters
    name = request.args.get('name')
    return f'Hello {name}, it\'s Flask here !!! Your Id is {id}'

if __name__ == '__main__':
    app.run(debug=True)