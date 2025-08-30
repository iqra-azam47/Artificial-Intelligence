import os
import openai
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv

# .env فائل سے API key لوڈ کریں
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# OpenAI کلائنٹ کو انیشیالائز کریں، جو OpenRouter کے ساتھ کام کرتا ہے
try:
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not found in .env file.")

    client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
except ValueError as e:
    print(f"Configuration error: {e}")
    client = None

app = Flask(__name__)

# ہوم پیج دکھانے کے لیے روٹ
@app.route('/')
def home():
    return render_template('index.html')

# چیٹ کا جواب دینے کے لیے روٹ
@app.route('/chat', methods=['POST'])
def chat_endpoint():
    user_message = request.json.get('message', '')
    
    # چیک کریں کہ کلائنٹ صحیح طرح سے انیشیالائز ہوا ہے
    if client is None:
        return jsonify({"reply": "Configuration error: API key is missing. Please check your .env file."})

    try:
        # OpenRouter API کو سوال بھیجیں
        response = client.chat.completions.create(
            # یہاں وہ ماڈل استعمال کریں جو آپ OpenRouter سے چاہتے ہیں
            # مثال کے طور پر: "openai/gpt-4o", "google/gemini-pro-1.5", "mistralai/mixtral-8x7b-instruct"
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_message}
            ],
            stream=False,
        )
        
        # جواب سے صرف متن نکالیں
        gemini_reply = response.choices[0].message.content

    except Exception as e:
        print(f"Error fetching response from OpenRouter: {e}")
        gemini_reply = "میں آپ کی درخواست پر کارروائی کرنے سے قاصر ہوں۔ براہ کرم دوبارہ کوشش کریں."

    return jsonify({"reply": gemini_reply})

if __name__ == '__main__':
    app.run(debug=True)