from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from url import CreateShortURL


app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def hello_world():
    return render_template("index.html")


protocol = 'http'
domain = 'localhost'


@app.route('/api/create_short_url', methods=['POST'])
def random_number():
    """
    Create short url.

    :return hort url
    """
    data = request.get_json()
    long_url = data['longurl']
    create_short = CreateShortURL(protocol, domain)
    url = create_short.get_url()




    return jsonify(data)
