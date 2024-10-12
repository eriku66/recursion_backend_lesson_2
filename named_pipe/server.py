import json
import os

config = json.load(open("config.json"))

filepath = config["filepath"]

if os.path.exists(filepath):
    os.remove(filepath)

dirpath = os.path.dirname(filepath)

if not os.path.exists(dirpath):
    os.makedirs(dirpath, 0o700)

os.mkfifo(filepath, 0o600)

print(f"FIFO named {filepath} is created successfully.")
print("Type in what you would like to send to clients.")


while True:
    inputstr = input()

    if inputstr == "exit":
        break
    else:
        with open(filepath, "w") as f:
            f.write(inputstr)

os.remove(filepath)
