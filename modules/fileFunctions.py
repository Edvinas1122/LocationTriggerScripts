import os

def save_address_to_file(address, location):
	with open(location, "w") as f:
		f.write(address)

def get_address_from_file(location):
	if os.path.exists(location):
		with open(location, "r") as f:
			return f.read().strip()
	else:
		return ""

def replace_file_contents(formatted_address, location):
	if formatted_address != get_address_from_file(location):
		save_address_to_file(formatted_address, location)
		print("Address updated: " + formatted_address)
		return True
	else:
		print("Address already up-to-date: " + formatted_address)
		return False