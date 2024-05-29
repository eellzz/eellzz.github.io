from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API configuration
ASSISTANT_ID = ""
API_KEY = ""

openai.api_key = API_KEY

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")

    try:
        response = openai.Completion.create(
            engine=ASSISTANT_ID,
            prompt=question,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        answer = response.choices[0].text.strip()
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False)
