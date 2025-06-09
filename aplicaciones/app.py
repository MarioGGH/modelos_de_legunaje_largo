import requests
import json
import web

urls = (
    '/', 'Index'
)

render = web.template.render('templates')
app = web.application(urls, globals())

class Index:
    def GET(self):
        return render.index()
    
    def ollama(self, prompt):
        try:
            data = {
                "model": "gemma3:1b",
                "prompt": prompt,
                "stream": False
            }
            url = "http://localhost:11434/api/generate"
            response = requests.post(url, json=data)
            response = json.loads(response.text)
            print(response["response"])
            response = response["response"]
            # Imprimimos la respuesta de la API
            # Retornamos la respuesta al template
            return render.index(response)
        except Exception as e:
            print(f"Error 001: {e}")
            
    def POST(self):
        formulario = web.input()
        prompt = formulario.inp_prompt
        
        print(f"Prompt recibido: {prompt}")
        return self.ollama(prompt)
    
if __name__ == "__main__":
    app.run()