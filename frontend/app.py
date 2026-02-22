from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Ankur this is frontend Frontend!"

if __name__ == "__main__":
    # Important: 0.0.0.0 pe run karo aur port 3000
    app.run(host="0.0.0.0", port=3000)

