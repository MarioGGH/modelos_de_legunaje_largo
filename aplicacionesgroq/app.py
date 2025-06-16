import web
import requests
import json

urls = (
    '/', 'Index'
)
render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def GET(self):
        return render.index()

    def groq(self, prompt):
        try:
            headers = {
                "Authorization" : "Bearer {YOUR_API_KEY}",
                "Content-Type" : "application/json"
            }
            data = {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                }
                ],
                "model": "meta-llama/llama-4-scout-17b-16e-instruct",
                "stream": False,
                "temperature": 1,
                "stop": None
            }
            url = "https://api.groq.com/openai/v1/chat/completions"
            response = requests.post(url, headers=headers, json=data)
            response = json.loads(response.text)
            print(response["choices"][0]["message"]["content"])
            response = response["choices"][0]["message"]["content"]
            # Imprimimos la respuesta de la API
            # Retornamos la respuesta al template
            return render.index(response)
        except Exception as e:
            print(f"Error 001: {e}")
            
    def POST(self):
        formulario = web.input()
        prompt = formulario.inp_prompt
        
        print(f"Prompt recibido: {prompt}")
        return self.groq(prompt)

if __name__ == "__main__":
    app.run()
