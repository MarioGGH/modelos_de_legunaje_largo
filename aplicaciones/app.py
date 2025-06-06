import requests

data = {
    "prompt" : "¿De que color es el cielo", 
    "model" : "gemma3:1b",
}
url = "http://localhost:11434/api/generate"

response = requests.post(url, json = data)

print(response.text)