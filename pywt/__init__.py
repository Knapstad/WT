import os
import json
import WT
if not os.path.exists("pywt/secrets"):
    os.makedirs("pywt/secrets")

config = {"proxies": None, "profile": None, "language": "en-GB", "format": "json", "auth": None, "verify": No

with open("pywt/secrets/config.txt", "w") as f:
	json.dump(config, f)

