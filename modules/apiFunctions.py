def	get_address_from_google_api(longitude, latitude, google_api_key):
	import requests

	# Send a request to the Geocoding API to get the address for the specified latitude and longitude
	url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={google_api_key}'
	response = requests.get(url)

	# Parse the response and extract the formatted address
	if response.status_code == 200:
		data = response.json()
		if data['status'] == 'OK':
			results = data['results']
			if len(results) > 0:
				formatted_address = results[0]['formatted_address']
				print(formatted_address)
		else:
			print(f"Geocoding API returned status: {data['status']}")
	else:
		print(f"Failed to connect to Geocoding API. Status code: {response.status_code}")
	return formatted_address

def logInto_iCloud(account_name, password):
	from pyicloud import PyiCloudService
	api = PyiCloudService(account_name, password)
	if api.requires_2sa:
		import click
		print("Two-step authentication required. Your trusted devices are:")

		devices = api.trusted_devices
		for i, device in enumerate(devices):
			print(
				"  %s: %s" % (i, device.get('deviceName',
				"SMS to %s" % device.get('phoneNumber')))
			)

		device = click.prompt('Which device would you like to use?', default=0)
		device = devices[device]
		if not api.send_verification_code(device):
			print("Failed to send verification code")
			sys.exit(1)

		code = click.prompt('Please enter validation code')
		if not api.validate_verification_code(device, code):
			print("Failed to verify verification code")
			sys.exit(1)
	return api

def	send_message_discord(message, channel_id, bot_token):
	import requests
	import json

	url = f"https://discord.com/api/channels/{channel_id}/messages"
	payload = {"content": message}
	headers = {
		"Authorization": f"Bot {bot_token}",
		"Content-Type": "application/json"
	}

	response = requests.post(url, data=json.dumps(payload), headers=headers)

	# Check the response status code to see if the request was successful
	if response.status_code == 200:
		print("Message sent: %s" % message)
	else:
		print("Message failed to send.")