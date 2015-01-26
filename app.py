from flask import Flask
app = Flask(__name__)

#for the slash rout run this function
@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
