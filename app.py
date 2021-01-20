#python as a programming language
#flask - web framework
#thonny - IDE
#MVC - model, view, controller

# --- Flask with dynamic variable ---#

# import the Flask class from the flask library

import sqlite3 as sql
from model import*
#from user_authentication import *
from flask import Flask,render_template,request,redirect,jsonify

# create the application object
app = Flask(__name__)

@app.route("/home")
def home():
    return render_template('homepage.html')

@app.route('/new_booking') #localhost:5000
def nbooking():
    rows=['']*2
    return render_template('booking_page.html', rows=rows)

@app.route('/list_booking') #localhost:5000
def lbooking():
    rows=list_booking()
    return render_template('list_booking.html', rows=rows)

@app.route('/list_space') #localhost:5000
def lspace():
    rows=list_space()
    return render_template('list_space.html', rows=rows)

@app.route('/update',methods=['GET','POST'])
def insert_booking():
    book_time_date = request.form['book_time_date']
    
    purpose=request.form['purpose']
          
    if request.method=="POST": 
      add_booking(book_time_date,purpose)
      return redirect('/list_booking')
    
    if request.method=='POST':                          
        row=['']*2
        row[0] = book_time_date
        row[1] = purpose

@app.route('/delete/<booking_id>')
def delete(booking_id):  
     delete_booking(booking_id)
     return redirect('/list_booking')
   
# start the server using the run() method
if __name__ == "__main__":
     app.secret_key = "!mzo53678912489"
     app.run(debug=True,host='0.0.0.0', port=5000)