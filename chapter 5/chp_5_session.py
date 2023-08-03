from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

#secret key is used to encrypt the session data
app.secret_key = "haseeb"

# The route() decorator tells Flask what URL should trigger the function.
@app.route("/")
def home():
    return render_template("index.html")


# GET and POST are the two types of HTTP requests.
@app.route("/login", methods=["POST", "GET"])
def login():
    if (request.method == "POST"):
        user = request.form["username"]
        #session is a dictionary that stores data across requests
        session["user"] = user
        return redirect(url_for("user"))
    else:
       return render_template("login.html")


#checking the session is created or not
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))




if (__name__ == "__main__"):
    app.run(debug=True)