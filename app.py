import os
import importlib
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
from datetime import datetime
from uuid import uuid4

import config

from flask import Flask,render_template, request, jsonify
 
app = Flask(__name__)

#############################################################
#############################################################

# Store API key in environment variable

bot_module = importlib.import_module(f"bots.chat_completion")
messages = bot_module.initialize_messages()

HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']

#############################################################
#############################################################

def create_dbitem(prompt):
    print ("success")
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY}, user_agent="CosmosDBPython", user_agent_overwrite=True)
    try:
        db = client.get_database_client(DATABASE_ID)
        container = db.get_container_client(CONTAINER_ID)
        item = { 'id': datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4()), 'prompt' : prompt }
        container.create_item(body=item)
    except exceptions.CosmosHttpResponseError as e:
            print('\nitem creation has caught an error. {0}'.format(e.message))
    finally:
            print("\item created")

@app.route('/')
def main():
    return render_template('home.html')


@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route("/ask", methods=['POST'])
def ask():
    message = str(request.form['messageText'])
    while True:
            bot_response = bot_module.return_response(messages, message)   
            return jsonify({'status':'OK','answer':bot_response})

@app.route("/create", methods=['POST'])
def create():
    print (request)
    prompt = str(request.form['promptText'])
    print ("success3")
    create_dbitem(prompt)
    return jsonify({'status':'OK','answer':'success'})


##app.run(host='localhost', port=5000)