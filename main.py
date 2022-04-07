from flask import Flask, Blueprint
from frontend.home import front_app

app = Flask(__name__)
app.register_blueprint(front_app)

if __name__ == '__main__':
    app.run(port=8765, debug=True)