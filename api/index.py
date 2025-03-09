from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
<<<<<<< HEAD
    return jsonify({"message": "Hey cool babe u can do it!"})
=======
    return jsonify({"message": "Hey cool babe you can do it"})
>>>>>>> 36fe28bc2690164d91c554e25f8b2523e39bfa6f

if __name__ == "__main__":
    app.run(debug=True)
