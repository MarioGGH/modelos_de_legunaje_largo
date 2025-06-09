# Modelos de legunaje largo

## 1. Descargar ollama
```sh
curl -fsSL https://ollama.com/install.sh | sh
```

## 3. Activar el servicio de ollama
```sh
ollama serve
```

## 4. Usar el modelo `gemma3:1b`
```sh
ollama pull gemma3:1b
```

## 5. Darle prompt a el modelo `gemma3:1b`
```sh
ollama run gemma3:1b "De que color es el cielo?"
```

## 6. Conectarse a la api de ollama
```sh
curl http://localhost:11434/api/generate -d '{
    "model": "gemma3:1b",
    "prompt":"De que color es el cielo?"
}'
```

## 7. Darle formato al json de la api
```sh
curl http://localhost:11434/api/generate -d '{
    "model": "gemma3:1b",
    "prompt":"Hola",
    "stream" : false
}'
```

## 8. Response de la api de ollama en nuestra pagina web
Para esto hemos de tener un archivo index.html el cual contendra un formulario, que consta de 4 elementos `<textarea>`, `<label>`, `<input>` y `<Button>`.

```html
<div class="form">
        <form method="POST">
            <textarea type="text" name="response" id="response" rows="30" cols="50" readonly>$response</textarea>
            <br>
            <label for="inp_promt">Prompt</label>
            <br>
            <input type="text" name="inp_promt" id="inp_promt" placeholder="prompt" required>
            <br>
            <button type="submit" name="generar">Generar</button>
        </form>
    </div>
```

Este html ira conectado a nuestro archivo app.py el cual recibira como parametros el `inp_promt`, este parametro se le asginara a la variable promt
```python
promt = formulario.inp_promt
```

dentro de nuetro diccionario el valor de prompt sera cambido por la variable del mismo nombre, pasando de ser una cadena a algo que el usuario pueda introducir a voluntad.
```python
data = {
            "model": "gemma3:1b",
            "prompt": promt,
            "stream": False
        }
```
Convertimos nuestro diccionario a un json y se lo pason al url de la api de ollama.
```python
url = "http://localhost:11434/api/generate"
response = requests.post(url, json = data)
```
Cargamos nuestro formato que le queremos dar a nuestro json.
```python
response = json.loads(response.text)
```

## 9. Retornamos nuestro response al html.
```python
return render.index(response=response["response"])
```

 # Uso de la API GroqCloud 
 Key API `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`

```sh
curl "https://api.groq.com/openai/v1/chat/completions" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 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" \
  -d '{
         "messages": [
           {
             "role": "user",
             "content": "1 + 1"
           }
         ],
         "model": "meta-llama/llama-4-scout-17b-16e-instruct",
         "temperature": 1,
         "max_completion_tokens": 1024,
         "top_p": 1,
         "stream": false,
         "stop": null
       }'
```