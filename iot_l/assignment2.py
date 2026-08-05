
from flask import Flask, request
from dbconnection import get_dbconnection as dbconn

server=Flask(__name__)

@server.get("/")
def homepage():
    return "Smart Home Monitoring System"

@server.post("/update")
def update_status():
    light=request.get_json().get("light")
    fan=request.get_json().get("fan")
    temperature=request.get_json().get("temperature")

    query=f"""
    insert into smarthome(light,fan,temperature)values('{light}','{fan}',{temperature});
    """
    conn=dbconn()
    cursor=conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

    return "Sensor data stored successfully"

@server.get("/status")
def get_status():
    query="""select * from smarthome order by temperature desc limit 1;"""

    conn=dbconn()
    cursor=conn.cursor()
    cursor.execute(query)
    status=cursor.fetchone()
    cursor.close()
    conn.close()

    return{
        "light":status[0],
        "fan":status[1],
        "temperature":status[2]
    }

if __name__ == "__main__":
    server.run(debug=True)
