from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
FROM_WHATSAPP = "whatsapp:+14155238886"   # Twilio sandbox
TO_WHATSAPP = "whatsapp:+96898978919"     # Your Oman number

@app.route("/tradingview/webhook", methods=["POST"])
def webhook():
    data = request.json

    message = f"""📊 TradingView Alert
Symbol: {data.get('symbol')}
Price: {data.get('price')}
Time: {data.get('time')}
"""

    url = f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json"
    payload = {
        "From": FROM_WHATSAPP,
        "To": TO_WHATSAPP,
        "Body": message
    }

    requests.post(url, data=payload, auth=(TWILIO_SID, TWILIO_TOKEN))
    return jsonify({"status": "ok"})
