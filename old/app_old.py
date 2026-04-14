# for run
# set FLASK_APP=app.py
# for MacOS or Linux
# export FLASK_APP=app.py
# python -m flask run
# for run over special ip (view in network) --host=[ip adress]
# python -m flask run --host=192.168.1.59

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route("/")
def hello_world():
    return '<p>Hello, World! <span style="color:red">from flask app inside docker container!!!</span></p>'

if __name__ == '__main__':
    app.run()