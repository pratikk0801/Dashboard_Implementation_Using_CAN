
from flask import Flask,request

from dbconnection import get_dbconnection as dbconn

server=Flask(__name__)

@server.get('/')
def homepage():
    return "Smart fuel station management system"

@server.post('/fuel')
def add_fuel():
    data = request.get_json()
    vehicle_no = data.get("vehicle_no")
    fuel_type = data.get("fuel_type")
    litres = data.get("litres")
    bill_amount = data.get("bill_amount")

    query=f"insert into fuelstation values('{vehicle_no}','{fuel_type}',{litres},{bill_amount});"
    conn=dbconn()
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return "vehical added successfully"

@server.get('/fuel')
def view_record():
    query="select * from fuelstation"
    conn=dbconn()
    cursor=conn.cursor()
    cursor.execute(query)
    fuelstation=cursor.fetchall()
    cursor.close()
    conn.close()

    return fuelstation

@server.route('/fuel' ,methods=['PUT'])
def update_data():
    vehicle_no=request.get_json().get('vehicle_no')

    query=f"update fuelstation set litres=27 where vehicle_no= '{vehicle_no}';"

    conn=dbconn()
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return "litres updated successfully"

@server.route('/fuel',methods=['DELETE'])
def delete_data():
    vehicle_no=request.get_json().get('vehicle_no')

    query=f"delete from fuelstation where vehicle_no='{vehicle_no}';"

    conn=dbconn()
    curser=conn.cursor()
    curser.execute(query)
    conn.commit()
    curser.close()
    conn.close()

    return "vehicle delerted successfully"



server.run(debug=True)