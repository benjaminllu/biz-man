from flask import Flask, request

app = Flask(__name__)

@app.route('/ebay-notify', methods=['POST'])
def ebay_webhook():
    data = request.json
    challenge_code = data.get('challengeCode')

    if challenge_code:
        return challenge_code, 200, {'Content-Type': 'text/plain'}
    else:
        return "No challenge code found", 400
