from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.get("/")
def test():
    return make_response(jsonify(status="ok", msg="Server is running...  test success"))


@app.get("/test")
def test2():
    return make_response(jsonify(status="ok", msg="test 2 request"))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
