from flask import Flask, redirect, url_for

app = Flask(__name__)

#defining the home page
@app.route("/")
def home():
    return "Hello, Flask!"
#defining a new page
@app.route("/user") 
def user():
    return "<h1> Hello, User! </h1>"

#passing in a variable
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
    return redirect(url_for("user", name="Admin!"))






if __name__ == '__main__':
    app.run()
