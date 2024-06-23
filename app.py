from flask import Flask, render_template, request, jsonify
from Core.rag_query import RAG

app = Flask(__name__)
rag = RAG()

def query(input):
    response = rag.chat_rag(input)
    print("Chat response:", response)
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    message = data.get('message')
    print("Received message:", message)
    response_message = query(message)
    print("response_message")
    response = {"response": response_message}
    print("Sending response:", response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
