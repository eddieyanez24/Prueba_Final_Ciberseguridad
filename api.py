from flask import Flask
from flask import request
from amigui_data_fetcher import get_item, set_item

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World</p>"


@app.route("/api/multiple")
def api_multiple():
    articulo = 20

    result = []
    for a in range(articulo):
        result.append(get_item(a))

    return result


@app.route("/api", methods=["GET"])
def get_api():
    articulo = 20

    result = []
    for a in range(articulo):
        result.append(get_item(a))
    result = dict(result)

    return get_item(result)


@app.route("/api", methods=["POST"])
def post_api():
    articulo = 20
    result = []
    for a in range(articulo):
        result.append(get_item(a))
    result = dict(result)

    return set_item(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3500, debug=True)
