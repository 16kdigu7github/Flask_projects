from flask import Blueprint, render_template, flash, redirect, request
from database import mongo

signupbp = Blueprint("signupbp", __name__, static_folder="static", template_folder="templates")


@signupbp.route("/", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template('signup.html')

    if request.method == "POST":
        passw =  request.form['pass']
        uname =  request.form['uname']     
        emai  =  request.form['emai']
        phno  =  request.form['phno']
        datav =  mongo.db.personal_data.find_one({"uname":uname})
        if datav:
            flash('user already exist')
            return redirect('/signup')
        else:
            mongo.db.personal_data.insert_one({'uname':uname,'pass':passw,'emai':emai,'phno':phno})
            flash('SIGN-UP SUCCESSFUL')
            return redirect('/login')