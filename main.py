
#DEPLOYED ON MICROSOFT AZURE :D
#!/usr/bin/python3
#needs AJAX ASAP
import flask
#import pymysql as sql
from flask import request
from threading import Thread


#db = sql.connect("sql7.freemysqlhosting.net", "sql7275673", "uvs94aUVZx","sql7275673")
#cursor = db.cursor()  #needs setting up one day
data = ["testmsgbultin"]

#Setup
web = flask.Flask('')

def run():
    web.run(host='0.0.0.0', port=8080)

def alive():
    t = Thread(target=run)
    t.start()
usernamea = "A User"  #Just a placeholder

@web.route('/')
def username():
  return flask.render_template('username.html')

#Setup END

#Get and Display number




#chocolate cookies
@web.route('/chat', methods=['POST'])
def chat():
    global resp

    try:
        request.form['nm']
        booleen = True
    except:
        booleen = False

    #if it works...
    # Dont fix it

    if booleen == True:
        user = request.form['nm']  #Get the wanted username
        resp = flask.make_response(
            flask.render_template('chat.html', data=data))  #Make a response
        resp.set_cookie('userID', user)  #Add the cookie

        return resp  #Return it

    else:
        if len(request.form['textin']) < 500:  #Check length

            data.append(
                request.cookies.get('userID') + " said: " +
                request.form['textin'])
            print(data)  #For debugging purposes

        return flask.render_template('chat.html', data=data)  #Return the page


alive()
#db.close()
#log.close()864787

#TODO LIST
# 1) Setup webserver   _/
# 2) Add messaging function in as raw a form as possible _/
# 2.5) Auto updating {{In Progress}} {{Maybe}}
# 3) Add user tags _/
# 4) Make it look good
# 5) Change tags to pre defined names (Accounts without sql)
# 6) Add accounts via SQL
# 7) Salt and hash time
# 8) Rooms with P/Ws
# 9) Finish the rest of hy
