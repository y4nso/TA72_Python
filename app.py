from flask import Flask, render_template, request, jsonify
from chatbot_logic import process_user_message, get_random_themes

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.get_json().get("question")
    bot_response = process_user_message(user_message)
    return jsonify({"answer": bot_response})

@app.route("/themes", methods=["GET"])
def themes():
    themes = get_random_themes()
    return jsonify({"themes": themes})

if __name__ == "__main__":
    app.run(debug=True)
