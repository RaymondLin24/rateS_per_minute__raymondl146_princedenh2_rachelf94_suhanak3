from flask import Flask, render_template, request, session #this one stores like everything
import os
import tiny, db_helpers
app = Flask(__name__)
app.secret_key = tiny.make()


@app.route("/",  methods=['GET'])
def register():
    if 'username' and 'password' in session:
        user = session['username']
        # pwd = session['password']
        # db_helpers.add_user(user, pwd)
        return render_template('homepage.html', name = user)
    return render_template( 'register.html' )


@app.route("/login",  methods=['GET','POST'])
def disp_loginpage():
    if 'username' and 'password' in session:
        user = session['username']
        return render_template('homepage.html', name = user)
    return render_template( 'login.html' ) #renders homepage


@app.route("/logout", methods = ['GET', 'POST'])
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return render_template('logout.html')


@app.route("/homepage", methods = ['GET', 'POST'])
def redirect():
    session['username'] = request.form['username']
    session['password'] = request.form['password']
    user = session['username']
    # pwd = session['password']
    # db_helpers.add_user(user, pwd)
    return render_template('homepage.html', name = user)

    return render_template( 'register.html' )


# @app.route("/login",  methods=['GET','POST'])
# def disp_loginpage():
#     if 'username' and 'password' in session:
#         user = session['username']
#         return render_template('homepage.html', name = user)
#     return render_template( 'login.html' ) #renders homepage


# @app.route("/logout", methods = ['GET', 'POST'])
# def logout():
#     session.pop('username', None)
#     session.pop('password', None)
#     return render_template('logout.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
