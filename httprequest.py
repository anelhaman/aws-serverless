import requests

def handler(event, context):
    r = requests.get("https://jsonplaceholder.typicode.com/users")
    return {"content": r.content}