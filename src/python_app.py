import os
from flask import Flask, jsonify, request, render_template

# Create an app for testing/interacting
app = Flask(__name__)
port = os.environ.get('PORT', 8080)

# Add routes to answer http requests
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['GET'])
def hello():
    if (request.method == 'GET'):
        data = "Hello from the Buildpacks Template"
        return jsonify({'data': data}), 200

@app.route('/funfact', methods=['GET'])
def funfact():
    funfact_data = 'Its Impossible to Hum While You Hold Your Nose (go ahead, we are all trying it)'
    return jsonify({'data': funfact_data}), 200

@app.route('/gen500', methods=['GET'])
def gen500():
    gen_500 = "500 - Web Server Error"
    return jsonify({'data': gen_500}), 500

@app.route('/gen404', methods=['GET'])
def gen404():
    gen_404 = "404 - This isn't the template you were looking for"
    return jsonify({'data': gen_404}), 404

# Do stuff
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=False)