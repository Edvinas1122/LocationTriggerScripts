# LocationTriggerScripts
Personal python scripts that triggers actions in a list based on current location
pragmatic for iPhone platform, but if ask I can deliver script for Android also :)

server comunicates messages via Discord platform

Dependencies:
  1. pip install openai
  2. pip install pyicloud==0.9.6.1
  3. other dependencies to be updated

API & Services registration required:
  1. Discord - only needs a server with a hook
  2. Google Geocode - https://developers.google.com/maps/documentation/geocoding/overview
  3. OpenAi - https://openai.com/blog/openai-api
  4. iCloud account - https://www.icloud.com/

Configs to update:
  1. _config.py -> config.py - must have api keys logins and passwords
  2. _addressList.json -> addressList.json  intended to contain list of triggerable addresses and acctions
 
Application idea structure in abstraction:
  1. Linux Server
  2. Phone location extraction
    2.1 Position Extraction 
    2.2 Position Translation into address, or business
  3. Information delivirence to users phone (discord, facebook mesanger, IRC server client...)
  4. A list of _address_ triggered actions()

Files:
  1. loopUpdateLocation.py -> runtime handle
  2. actions.py -> holds triggarable actions

about programming style:
  _writen in functional hierarchical modular style. It's them scripts after all._