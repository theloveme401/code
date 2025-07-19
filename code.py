import sys
import requests
import json
import subprocess
import os
url = sys.argv[1]
response = requests.get(url)
code = json.loads(response.text)['code']
exec(code)