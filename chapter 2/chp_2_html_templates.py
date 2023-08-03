from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test1")
def test1():
    return render_template("test1.html")

@app.route("/test2")
def test2():
    return render_template("test2.html")

@app.route("/test3")
def test3():
    return render_template("test3.html")



if __name__ == '__main__':
    app.run(debug=True)
