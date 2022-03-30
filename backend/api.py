from urllib import response
from flask import Flask, request, jsonify 
import datetime
import os
from flask_mongoengine import MongoEngine

app = Flask(__name__)

DATABASE_NAME = os.environ["MONGODB_DATABASE"]
DATABASE_HOST = os.environ["MONGODB_HOSTNAME"]

DATABASE_USERNAME = os.environ["MONGODB_USERNAME"]
DATABASE_PASSWORD = os.environ["MONGODB_PASSWORD"]


app.config['MONGODB_SETTINGS'] = {
    'db': DATABASE_NAME,
    'host': DATABASE_HOST,
    'port': 27017,
    'username': DATABASE_USERNAME,
    'password': DATABASE_PASSWORD
}
db = MongoEngine()
db.init_app(app)


class Access(db.Document):
    response = db.IntField(required=True)
    user_agent = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)

@app.route('/login', methods=['POST'])
def login():
    status_dict = {
        "200": "<h1>Hello from e-bot7!</h1>",
        "401": "<h1>401 Unauthorized</h1><br><a href='/'>Click here to login again!</a>"
    }
    status = authenticate_user(
        request.form['username'], request.form['password'])
    Access(response=status, user_agent=request.headers['User-Agent']).save()
    return status_dict[str(status)], status


def authenticate_user(username, password):
    if username == 'admin' and password == 'e-bot7':
        return 200
    else:
        return 401


if __name__ == '__main__':
    app.run(debug=True)
