import json
import os

config = json.load(open("config.json"))

filepath = config["filepath"]

if not os.path.exists(filepath):
    print("Server is not running.")
    exit(0)

f = open(filepath, "r")

while os.path.exists(filepath):
    data = f.read()

    if len(data) != 0:
        print(f"Data received from pipe: {data}")

f.close()
