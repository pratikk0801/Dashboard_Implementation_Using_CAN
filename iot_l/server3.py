
from flask import Flask

srv=Flask(__name__)

temps=list()

@srv.get('/')
def homepage():
    return "this is homepage"

@srv.get('/temperatures')
def get_tenmperatures():
  #  temps=[28.0,29.2,32.1,22.8,25.8]
    return f"temps = {temps}"

@srv.post('/temperatures/<float:temp>')
def add_temperature(temp):
    temps.append(temp)
    return f"{temp} temperature is received"

if __name__ == '__main__':
    srv.run(debug=True)

