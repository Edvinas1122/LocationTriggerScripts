def handleAddressTriggerAction(formatted_address, addressListFileLocation):
	import json
	with open(addressListFileLocation) as json_file:
		addressList = json.load(json_file)["addresses"]
		for entry in addressList:
			if formatted_address == entry["address"]:
				action = entry["action"]
				parameters = entry.get("parameters", {})
				execute_action(action, parameters)

def execute_action(action, parameters):
	if action == "call_chatGPT_api":
		request = parameters.get("request", 1)
		count = parameters.get("responses", 1)
		call_chatGPT_api(request, count)
	elif action == "getShopOffers":
		getShopOffers()
	elif action == "another_action":
		param1 = parameters.get("param1")
		param2 = parameters.get("param2")
		another_action(param1, param2)

	# Add more conditionals for other actions as needed

from modules.apiFunctions import send_message_discord
from config.config import bot_token, channel_id, organization
from modules.scrapPage import getPennyFoodOffers

def call_chatGPT_api(request, response_count, max_token_count=30):
	from config.config import chatGPT_api_key
	from modules.chatGPT_functions import getResponse

	responses = getResponse(request, response_count, chatGPT_api_key, organization, max_token_count)
	for response in responses:
		send_message_discord(response, channel_id, bot_token)

def getShopOffers():
	offers = getPennyFoodOffers()
	for offer in offers:
		send_message_discord(offer, channel_id, bot_token)

def another_action(param1, param2):
	# Logic for another_action with the provided parameters
	print("Executing another action:", param1, param2)
