from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():


    return "这是主页面"


if __name__ == "__main__":
    app.run()
