from models.user import User

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

users = []

@app.route('/api/v1', methods=['GET'])
def view_routes():
    routes = {
        "View API": "GET /api/v1",
        "Create User": "POST /api/v1/user"
    }

    return jsonify(routes)

@app.route('/api/v1/user', methods=['POST'])
def create_user():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    location = request.form['location']

    user = User(name, age, email, location)
    users.append(user)

    return "Created new user:\n{}\n".format(user)


@app.route('/hello/<userId>', methods=['GET'])
def hello_page(userId):
    hello = "Hello {}\n".format(userId)
    for user in users:
        if(user.userId == userId):
            hello = "Hello,\n{user}\n".format(user=user)

    return hello

@app.route('/')
def index():
    return render_template("index.html")

def main():
    app.run()

if __name__ == '__main__':
    main()