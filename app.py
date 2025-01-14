from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "Your Open Ai Key"

# Load documentation links
DOCUMENTATION_LINKS = {
    "segment": "https://segment.com/docs/?ref=nav",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}


@app.route('/ask', methods=['POST'])
def ask_question():
    user_input = request.json.get('question', '')
    platform = request.json.get('platform', '').lower()

    if platform not in DOCUMENTATION_LINKS:
        return jsonify({"error": "Unsupported platform. Choose from Segment, mParticle, Lytics, Zeotap."}), 400

    documentation_url = DOCUMENTATION_LINKS[platform]

    # Use OpenAI API to generate a response
    prompt = (
    f"You are a helpful chatbot assisting with Customer Data Platforms. Using the official documentation "
    f"available here: {documentation_url}, answer the following question:\n"
    f"Question: {user_input}\n"
    f"Provide a step-by-step guide if applicable or direct link references."
)


    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.5
    )

    answer = response.choices[0].text.strip()
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
