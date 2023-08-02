from flask import Flask, redirect, url_for

app = Flask(__name__)

#routing different pages 
@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/user") 
def user():
    return "<h1> Hello, User! </h1>"

#what user passes in the url will be passed to the function as an argument and returned
@app.route("/<member>")
def member(member):
    return f"Hello, {member}!"

#passing in an integer
@app.route("/<int:member_id>")
def member_id(member_id):
    return f"Member ID: {member_id}"
    
#redirecting to another page    
@app.route("/admin")
def admin():
    #defing the function to redirect to in return
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run()