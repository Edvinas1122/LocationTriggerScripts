def checkIfUpdatedLocation(location):
    if not hasattr(checkIfUpdatedLocation, 'previous_location'):
        # Initialize the static variable on the first function call
        checkIfUpdatedLocation.previous_location = {'latitude': 0.0, 'longitude': 0.0}

    if (location['latitude'] == checkIfUpdatedLocation.previous_location['latitude'] and
            location['longitude'] == checkIfUpdatedLocation.previous_location['longitude']):
        return False
    else:
        checkIfUpdatedLocation.previous_location = location  # Update the static variable
        return True

def addressInAMapOfTriggerActions(formatted_address, addressListFileLocation):
    import json
    with open(addressListFileLocation) as json_file:
        addressList = json.load(json_file)["addresses"]
        for entry in addressList:
            if formatted_address == entry["address"]:
                return True
    return False
