import sqlite3 as sql

from functools import wraps
from flask import session,flash,redirect,url_for

connect_db ='moms.db'

def list_booking():
  with sql.connect(connect_db) as db:
    qry = 'SELECT booking_id, book_time_date, purpose, space_name FROM booking INNER JOIN space ON booking.space_id=space.space_id' 
    result=db.execute(qry)
    return(result)

def list_space():
  with sql.connect(connect_db) as db:
    qry = 'select * from space' 
    result=db.execute(qry)
    return(result)

def result():
  rows=list_booking()
  rows=list_space()
  for row in rows:
      print (row)

def add_booking(book_time_date,purpose,space_id):
  with sql.connect(connect_db) as db:
    qry='insert into booking (book_time_date,purpose,space_id) values (?,?,?)' 
    db.execute(qry,(book_time_date,purpose,space_id))

# helper function

def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
        return f(*args, **kwargs)
    else:
        flash("You need to login first")
        return redirect(url_for('home'))
  return wrap

def update_booking(book_time_date, purpose,space_id):
  with sql.connect(connect_db) as db:
    qry='insert into booking (book_time_date,purpose,space_id) values (?,?,?)' 
    db.execute(qry,(book_time_date,purpose,space_id))

def delete_booking(booking_id):
  with sql.connect(connect_db) as db:
    qry='delete from booking where booking_id=?' 
    db.execute(qry,(booking_id,))

def availability(space_id,book_time_date):
  with sql.connect(connect_db) as db:
    qry = 'SELECT space_id,book_time_date FROM booking  where space_id=? and book_time_date=? '
    result=db.execute(qry,(space_id,book_time_date)).fetchone()
    return(result)