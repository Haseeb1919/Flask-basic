from flask import Flask, redirect, url_for, render_template, request, session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#secret key is used to encrypt the session data
app.secret_key = "haseeb"

#configuring the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


#storing the permanent session data 
app.permanent_session_lifetime = timedelta(minutes=5)


#initializing the database
db = SQLAlchemy(app)

#creating the model
class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


    def __init__(self, name, email):
        self.name = name
        self.email = email


# The route() decorator tells Flask what URL should trigger the function.
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())


# GET and POST are the two types of HTTP requests.
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["username"]
        email = request.form["email"]
        # Session is a dictionary that stores data across requests
        session["user"] = user
        session["email"] = email  # Store the email in the session
        flash(f"Login Successful! {user}", "info")

        found_user = users.query.filter_by(name=user).first()
        # Adding user to the database and checking if the user already exists
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, email)  # Store the email in the database
            db.session.add(usr)
        db.session.commit()

        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!", "info")
            return redirect(url_for("user"))
        return render_template("login.html")


#checking the session is created or not
@app.route("/user", methods=["GET"])
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", email=session.get("email"))
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
    session.pop("email", None)
    
    return redirect(url_for("login"))

if (__name__ == "__main__"):
    with app.app_context():
        db.create_all()
        app.run(debug=True)