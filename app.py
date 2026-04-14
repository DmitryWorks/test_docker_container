# for run
# set FLASK_APP=app.py
# for MacOS or Linux
# export FLASK_APP=app.py
# python -m flask run
# for run over special ip (view in network) --host=[ip adress]
# python -m flask run --host=192.168.1.59

from flask import Flask
import yaml

# Load YAML config file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

app_name = config['app']['name']
app_version = config['app']['version']
app_message = config['app']['message']
host = config['app_config']['host']
port = config['app_config']['port']

print('config data: ', app_name, app_version, host, port, app_message)

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route("/")
def hello_world():
    return f'<p>Hello, World! {app_name} <span style="color:red"> {app_version}</span>, Application message: "{app_message}"</p>'

if __name__ == '__main__':
    app.run()
