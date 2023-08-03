from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# The route() decorator tells Flask what URL should trigger the function.
@app.route("/")
def home():
    return render_template("index.html")


# GET and POST are the two types of HTTP requests.
@app.route("/login", methods=["POST", "GET"])
def login():
    if (request.method == "POST"):
        user = request.form["username"]
        return redirect(url_for("user", usr=user))
    else:
       return render_template("login.html")


# The <usr> is a variable that can be used in the function.
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"



if (__name__ == "__main__"):
    app.run(debug=True)