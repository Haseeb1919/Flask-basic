from flask import Flask, redirect, url_for, render_template, request, session,flash
from datetime import timedelta

app = Flask(__name__)

#secret key is used to encrypt the session data
app.secret_key = "haseeb"
#storing the permanent session data 
app.permanent_session_lifetime = timedelta(minutes=5)

# The route() decorator tells Flask what URL should trigger the function.
@app.route("/")
def home():
    return render_template("index.html")


# GET and POST are the two types of HTTP requests.
@app.route("/login", methods=["POST", "GET"])
def login():
    if (request.method == "POST"):
        session.permanent = True
        user = request.form["username"]
        #session is a dictionary that stores data across requests
        session["user"] = user
        flash(f"Login Successful! {user}", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!", "info")
            return redirect(url_for("user"))

        return render_template("login.html")


#checking the session is created or not
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!", "info")
        return redirect(url_for("login"))


#deleting the session
@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out! {user}" , "info")
    session.pop("user", None)
    
    return redirect(url_for("login"))

if (__name__ == "__main__"):
    app.run(debug=True)