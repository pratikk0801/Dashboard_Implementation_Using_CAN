
from flask import Flask, request

from dbconnection import get_dbconnection as dbconn

server=Flask(__name__)

@server.get('/')
def homepage():
    return "Student Management System"

@server.get('/students')
def get_students():
    conn=dbconn()
    query="select * from studinfo;"
    cursor=conn.cursor()
    cursor.execute(query)
    studs=cursor.fetchall()
    cursor.close()
    conn.close()

    return f"students={studs}"

@server.post('/student')
def insert_student():
    roll_no=request.form.get('roll_no')
    name=request.form.get('name')
    course=request.form.get('course')
    marks=request.form.get('marks')

    query=f"insert into studinfo values({roll_no},'{name}','{course}',{marks});"

    conn=dbconn()
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return f"Student with rollno {roll_no} is added successfully"
 
@server.route('/student',methods=['PUT'])
def update_student():
    roll_no=request.form.get('roll_no')
    marks=request.form.get('marks')

    query=f"update studinfo set marks={marks} where roll_no = {roll_no};"


    conn=dbconn()
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return f"Student with roll_no {roll_no} is updated successfully"

@server.route('/student',methods=['DELETE'])
def delete_student():
    roll_no=request.form.get('roll_no')

    query=f"delete from studinfo where roll_no = {roll_no};"


    conn=dbconn()
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return f"Student with roll_no {roll_no} is deleted successfully"

server.run(debug=True)
