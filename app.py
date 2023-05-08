import os
import importlib

from flask import Flask,render_template, request, jsonify
 
app = Flask(__name__)

#############################################################
#############################################################

# Store API key in environment variable
os.environ['OPENAI_API_KEY'] = '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'

bot_module = importlib.import_module(f"bots.chat_completion")
messages = bot_module.initialize_messages()


#############################################################
#############################################################
 
@app.route('/')
def hello():
    return render_template('chat.html')


@app.route("/ask", methods=['POST'])
def ask():
    message = str(request.form['messageText'])
    while True:
            bot_response = bot_module.return_response(messages, message)   
            return jsonify({'status':'OK','answer':bot_response})

app.run(host='localhost', port=5000)