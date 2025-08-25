# Clarify
JSON parser for Spotify user history, poorly written in Python.

# How to Use
You can get the JSONs this script parses from Spotify by requesting your user data on the Spotify website. I believe both past-year and lifetime data requests are compatible!
You will find the array `target_jsons` at the bottom of the script. By default, it contains one target, `./StreamingHistory0.py`.
This script was designed with scalability in mind, if you have more jsons (you likely will), feel free to add them to the array. It is recommended to order the array chronologically.
