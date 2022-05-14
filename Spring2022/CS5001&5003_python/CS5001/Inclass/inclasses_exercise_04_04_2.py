"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""

# Python program to write JSON
# to a file

import json

# Data to be written
dictionary = {
    "name": "jason",
    "height": 56,
    "weight": 212,
    "phone number": "9976770500",
    "color Scheme": "purple"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as f:
    f.write(json_object)
