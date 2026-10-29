import urllib.request
import json
import sys


if len(sys.argv) < 2:
    print("Error: please provide a GitHub username")
    print("Usage: python github_activity.py <username>")
    print("Example: python github_activity.py kamranahmedse")
    sys.exit()

user_name = sys.argv[1]
URL = f"https://api.github.com/users/{user_name}/events"

    

with urllib.request.urlopen(URL) as response:
    raw = response.read()

# print(type(raw))

text = raw.decode("utf-8")
# print(type(text))

events = json.loads(text)



for event in events:
    if event["type"] == "PushEvent":
        print(f"- Pushed to {event["repo"]["name"]}")

    elif event["type"] == "WatchEvent":  
        print(f"- Starred {event["repo"]["name"]}")

    elif event["type"] == "CreateEvent":  
        print(f"- Created {event["repo"]["name"]}")    

    elif event["type"] == "IssuesEvent":  
        print(f"- Opened an issue in {event["repo"]["name"]}")

    elif event["type"] == "ForkEvent":  
        print(f"- Forked {event["repo"]["name"]}") 
    else:
        print(f"- {event["type"]} in {event["repo"]["name"]}")
    