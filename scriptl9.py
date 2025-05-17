from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFICATION_KEY = "Apple-Orchard-Banana-Cat-Dance86638663"

@app.route('/ebay-notify', methods=['POST'])
def ebay_notify():
    try:
        data = request.get_json()
        challenge_code = data.get("challengeCode")

        if challenge_code:
            return jsonify({
                "challengeResponse": challenge_code,
                "verificationKey": VERIFICATION_KEY
            }), 200
        else:
            return jsonify({"error": "Missing challengeCode"}), 400
    except Exception as e:
        print("Webhook error:", str(e))
        return jsonify({"error": "Server error"}), 500

@app.route('/ebay-notify', methods=['GET'])
def ebay_notify_get():
    return "OK", 200
