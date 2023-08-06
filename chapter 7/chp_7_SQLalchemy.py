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
    if (request.method == "POST"):
        session.permanent = True
        user = request.form["username"]
        #session is a dictionary that stores data across requests
        session["user"] = user
        flash(f"Login Successful! {user}", "info")


        found_user = users.query.filter_by(name=user).first()
        #adding user to the database and checking if the user already exists
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()


                
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!", "info")
            return redirect(url_for("user"))
        return render_template("login.html")





#checking the session is created or not
@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if (request.method == "POST"):
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!", "info")

        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
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