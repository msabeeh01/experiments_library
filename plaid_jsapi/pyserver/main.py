import flask
from flask import Flask, jsonify, json, request as REQ
from flask_cors import CORS

import logging
logging.basicConfig(level=logging.DEBUG)

import plaid
from plaid_client import plaid_client
from plaid.model.products import Products

from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.country_code import CountryCode
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser

app = flask.Flask(__name__)
CORS(app)

# TODO: store these values in a more secure way for the serverside to access whenever calling plaid enpoints
access_token = None
item_id = None


@app.route('/exchange_public_token', methods=['POST'])
def exchange_public_token():
    global access_token
    public_token = REQ.get_json()['public_token']
    request = ItemPublicTokenExchangeRequest(
      public_token=public_token
    )
    response = plaid_client.item_public_token_exchange(request)
    # These values should be saved to a persistent database and
    # associated with the currently signed-in user
    access_token = response['access_token']
    item_id = response['item_id']
    return jsonify({'public_token_exchange': 'complete'})

# get accesstoken
@app.route("/create_link_token", methods=['POST'])
def create_link_token():
    # Get the client_user_id by searching for the current user
    client_user_id = 'placeholder'
    # Create a link_token for the given user
    request = LinkTokenCreateRequest(
            products=[Products("auth")],
            client_name="Plaid Test App",
            country_codes=[CountryCode('CA')],
            redirect_uri='http://localhost:3000',
            language='en',
            webhook='https://webhook.example.com',
            user=LinkTokenCreateRequestUser(
                client_user_id=client_user_id
            )
        )
    response = plaid_client.link_token_create(request)
    # Send the data to the client
    return jsonify(response.to_dict())


@app.route('/accounts', methods=['GET'])
def get_accounts():
  try:
      request = AccountsGetRequest(
          access_token=access_token
      )
      accounts_response = plaid_client.accounts_get(request)
  except plaid.ApiException as e:
      response = json.loads(e.body)
      return jsonify({'error': {'status_code': e.status, 'display_message':
                      response['error_message'], 'error_code': response['error_code'], 'error_type': response['error_type']}})
  return jsonify(accounts_response.to_dict())


