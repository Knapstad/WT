import os
import json

if not os.path.exists("pywt/secrets"):
    os.makedirs("pywt/secrets")

config_ = {"proxies": None, "profile": None, "language": "en-GB",
           "format_": "json", "auth": None, "verify": None}


json.dump(config_, open("pywt/secrets/config.json", "w"))
