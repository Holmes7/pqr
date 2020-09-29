from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/login")
def login():
	return "login1"


if __name__ == "__main__":
	app.run(debug=True)
