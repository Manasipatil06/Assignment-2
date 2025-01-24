
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Example URLs for CDP documentation
CDP_DOCS = {
    "segment": "https://segment.com/docs/",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question', '')
    cdp = request.json.get('cdp', '').lower()
    
    if cdp in CDP_DOCS:
        response = {
            "message": f"Fetching information from {CDP_DOCS[cdp]} related to: {user_question}"
        }
    else:
        response = {
            "message": "Please specify a valid CDP (Segment, mParticle, Lytics, Zeotap)."
        }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
