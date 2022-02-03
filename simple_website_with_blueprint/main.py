
#libraries
from flask import Flask, render_template, request, flash, redirect, session
from database import mongo
from signup.signuppage import signupbp
from login.loginpage import loginbp
from home.homepage import homebp

app = Flask(__name__)

app.secret_key = "$a.0.j.0.a.0.y.likes_starwars#@!"
app.config['MONGO_URI'] = "mongodb://localhost:27017/user_data"
mongo.init_app(app)

app.register_blueprint(signupbp, url_prefix="/signup")
app.register_blueprint(loginbp, url_prefix="/login")
app.register_blueprint(homebp, url_prefix="/home")


@app.route("/")
def main():
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)