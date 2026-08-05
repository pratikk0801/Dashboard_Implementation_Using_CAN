

import mysql.connector

def get_dbconnection():
    connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        database='iotfeb24',
        user='sunbeam',
        password='sunbeam@123'
    )

    return connection;