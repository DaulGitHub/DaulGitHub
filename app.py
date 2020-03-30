from flask import Flask, render_template, jsonify, request, g
from flask_cors import CORS
from url import CreateShortURL
from dataaccess.db_getaway import Storage


app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
app.config.from_object('config.dev.DevelopmentConfig')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


def get_db():
    if not hasattr(g, 'storage'):
        g.storage = Storage(app.config['DB_NAME'], app.config['DB_USER'], app.config['DB_HOST'], app.config['DB_PASSWORD'])
    return g.storage


@app.before_request
def before_request():
    g.storage = get_db()


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/api/create_short_url', methods=['POST'])
def random_number():
    """
    Create short url.

    :return short url
    """
    data = request.get_json()
    long_url = data['longurl']
    create_short = CreateShortURL(app.config['PROTOCOL'], app.config['DOMAIN'])
    short_url = create_short.get_url()

    g.storage.save_url(long_url, short_url)

    return jsonify({'short': short_url})
