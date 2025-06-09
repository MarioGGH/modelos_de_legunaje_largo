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
    
    def POST(self):
        #Obtenemos lo introducido en el formulario
        formulario = web.input()
        #Lo imprimimos para saber si fue recibido de forma correcta
        print("Recibiendo datos del formulario")
        print("Log:", formulario)
        
        #Recibimos el prompt
        #Imprimimos el prompt
        promt = formulario.inp_promt
        print("Prompt:", promt)
        
        #Hacemos un diccionario con los paramatros necesarios para la API
        data = {
            "model": "gemma3:1b",
            "prompt": promt,
            "stream": False
        }
        
        url = "http://localhost:11434/api/generate"
        # Al response se le asigna los datos dentro de nuestro diccionario data
        # Tambien hemos de convertir nuestros datos a un json
        response = requests.post(url, json = data)
        response = json.loads(response.text)
        print(response["response"])
        # Retornamos la respuesta al template
        return render.index(response=response["response"])

if __name__ == "__main__":
    app.run()