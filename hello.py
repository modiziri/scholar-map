from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/<username>")
def hello(username = 'Flask'):
    return render_template('index.html', name=username)

if __name__ == "__main__":
    app.run(debug=True)
