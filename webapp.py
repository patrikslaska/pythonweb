from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return get_content()

def get_content():
    # Implemement DB support later
    return "HELLO THE WORLD!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
