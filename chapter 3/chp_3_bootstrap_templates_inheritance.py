from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("testing.html")

@app.route("/test2")
def test2():
    return render_template("testing2.html")


if __name__ == '__main__':
    app.run(debug=True)     

  