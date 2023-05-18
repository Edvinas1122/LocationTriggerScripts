# LocationTriggerScripts
Personal python scripts triggers actions in a list based on current location
pragmatic for iPhone platform, but if ask I can deliver script for Android also :)

server comunicates messages via Discord platform

Dependencies:
  pip install openai
  pip install pyicloud==0.9.6.1
  other dependencies to be updated

API & Services registration required:
  Discord - only needs a server with a hook
  Google Geocode - https://developers.google.com/maps/documentation/geocoding/overview
  OpenAi - https://openai.com/blog/openai-api
  iCloud account - https://www.icloud.com/

Configs to update:
  _config.py -> config.py - must have api keys logins and passwords
  _addressList.json -> addressList.json  intended to contain list of triggerable addresses and acctions
 
 Application idea structure in abstraction
  1. Linux Server
  2. Phone location extraction
    2.1 Position Extraction 
    2.2 Position Translation into address, or business
  3. Information delivirence to users phone (discord, facebook mesanger, IRC server client...)
  4. A list of _address_ triggered actions()
