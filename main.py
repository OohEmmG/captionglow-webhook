from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if mode == "subscribe" and token == "captionglow_token":
            return challenge, 200
        else:
            return "Forbidden", 403
    elif request.method == "POST":
        data = request.get_json()
        print("Received webhook data:", data)
        return "EVENT_RECEIVED", 200