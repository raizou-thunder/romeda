import flask
import requests

app = flask.Flask(__name__, static_folder='static')

@app.route('/')
def index():
    response = requests.get('https://app.dissoku.net/api/guilds/?ordering=-exp,-upped_at&page=1&lang=ja')

    rank = 1
    for guild in response.json()['results']:
        if guild['id'] == '1187388265720979486':
            break
        rank += 1
    return flask.render_template('index.html', dissoku_rank=rank)

@app.route('/api/dissoku_rank')
def dissoku_rank():
    response = requests.get('https://app.dissoku.net/api/guilds/?ordering=-exp,-upped_at&page=1&lang=ja')

    rank = 1
    for guild in response.json()['results']:
        if guild['id'] == '1187388265720979486':
            break
        rank += 1
    return f'{rank}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)