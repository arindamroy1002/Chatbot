CDP Support Agent Chatbot

Overview

This chatbot is designed to answer "how-to" questions related to four popular Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. It retrieves relevant information from the official documentation of these platforms to guide users in performing tasks or configuring features.

Technologies Used

Python

Flask: Web framework for handling requests

OpenAI API: For natural language processing and generating responses

Prerequisites

Python 3.x

Dependencies listed in requirements.txt (Flask, OpenAI)

An OpenAI API key

Installation

Clone the repository:

git clone https://github.com/your-repo/chatbot
cd chatbot

Install dependencies:

pip install -r requirements.txt

Set up your OpenAI API key:

Replace YOUR_OPENAI_API_KEY in app.py with your actual API key.

Optional: Store the API key in an environment variable for security:

export OPENAI_API_KEY=your_key_here  # macOS/Linux
set OPENAI_API_KEY=your_key_here     # Windows

Running the Chatbot

Start the Flask application:

python app.py

The chatbot will run locally at: http://127.0.0.1:5000.

Example Request

Use curl or Postman to test the chatbot:

Using curl

curl -X POST http://127.0.0.1:5000/ask \
-H "Content-Type: application/json" \
-d '{"question": "How do I set up a new source in Segment?", "platform": "segment"}'

Using Postman

Set the request method to POST.

Enter the URL: http://127.0.0.1:5000/ask.

In the Body tab, choose raw and select JSON.

Enter this JSON:

{
  "question": "How do I set up a new source in Segment?",
  "platform": "segment"
}

Click Send.

Expected Output

The chatbot will return a response with step-by-step guidance or relevant information from the official documentation.

Sample Response

{
  "answer": "To set up a new source in Segment, follow these steps: ..."
}

Limitations

This chatbot depends on OpenAI's text model, which may not always provide fully accurate instructions.

The current implementation uses documentation URLs as context without directly scraping content.

Future Enhancements

Implement direct documentation scraping or indexing.

Add advanced handling for cross-platform comparisons and complex queries.

Integrate a UI for a better user experience.

License

This project is licensed under the MIT License.

