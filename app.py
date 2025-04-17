#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# app.py
from flask import Flask, request, jsonify
import string

app = Flask(__name__)

# Your API Key (share with your friend)
API_KEY = "12345"

# Function logic
def add_punctuation(data):
    return str(data) + string.punctuation

@app.route('/process', methods=['POST'])
def process():
    # Check API key
    key = request.headers.get('x-api-key')
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    # Get input JSON
    input_data = request.get_json()
    text = input_data.get("text", "")

    # Process the text
    result = add_punctuation(text)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)




# In[ ]:




