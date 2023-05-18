import time
import pprint
from modules.apiFunctions import *
from modules.fileFunctions import *
from modules.utilFunctions import checkIfUpdatedLocation, addressInAMapOfTriggerActions
from actions import handleAddressTriggerAction
#configurations required for running the service
from config.config import icloud_email, password, google_api_key, bot_token, channel_id

#update file with address
addressListFileLocation = "config/addressList.json"

text_file_location = "log/address.txt"

api = logInto_iCloud(icloud_email, password)
pprint.pprint(api.devices)
while True:
	location = api.devices[1].location() # is currently hardcoded to the first device in the list
	if (checkIfUpdatedLocation(location)):
		try:
			formatted_address = get_address_from_google_api(location['longitude'], location['latitude'], google_api_key)
			if (replace_file_contents(formatted_address, text_file_location)):
				if (addressInAMapOfTriggerActions(formatted_address, addressListFileLocation)):
					handleAddressTriggerAction(formatted_address, addressListFileLocation)
				else:
					send_message_discord(formatted_address, channel_id, bot_token)
		except Exception as e:
			send_message_discord("Failed to connect to Geocoding API:" + str(e), channel_id, bot_token)
	time.sleep(60)
