import urllib.request
import json

URL = "https://api.github.com/users/ademadem05/events"
with urllib.request.urlopen(URL) as response:
    raw = response.read()

# print(type(raw))

text = raw.decode("utf-8")
# print(type(text))

events = json.loads(text)


# print(events["type"]["payload"])
for event in events:
    # print(f"{event["repo"]["name"]}, {event["type"]}, {event["created_at"]}")
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
    