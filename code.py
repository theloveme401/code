url = sys.argv[1]
import requests
import json
import subprocess
response = requests.get(url)
code = json.loads(response.text)['code']
with open("code.py", "w") as f:
    f.write(code)
subprocess.run(["python3", "code.py"])
