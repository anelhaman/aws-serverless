import requests
import json

def handler(event, context):
    r = requests.get("https://jsonplaceholder.typicode.com/comments")
    return {"content": json.loads(r.content)}