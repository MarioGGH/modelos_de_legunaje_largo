# 🧠 Modelos de Lenguaje Local y API GroqCloud

Este proyecto demuestra cómo ejecutar modelos de lenguaje localmente con [Ollama](https://ollama.com) y cómo interactuar con la API de GroqCloud para generar respuestas a partir de prompts personalizados.

---

## 🧩 1. Instalación de Ollama

Instala Ollama ejecutando el siguiente comando:

```sh
curl -fsSL https://ollama.com/install.sh | sh
```

---

## 🚀 2. Iniciar el servicio de Ollama

```sh
ollama serve
```

---

## 📦 3. Descargar el modelo `gemma3:1b`

```sh
ollama pull gemma3:1b
```

---

## 💬 4. Ejecutar un prompt con el modelo `gemma3:1b`

```sh
ollama run gemma3:1b "¿De qué color es el cielo?"
```

---

## 🌐 5. Usar la API local de Ollama

Puedes generar respuestas directamente desde la API local:

```sh
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt": "¿De qué color es el cielo?"
}'
```

### 🎯 Con formato JSON (sin streaming):

```sh
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt": "Hola",
  "stream": false
}'
```

---

## 🧪 6. Integración en una página web

Crea un formulario en `index.html` para enviar prompts y mostrar respuestas:

```html
<div class="form">
  <form method="POST">
    <textarea name="response" id="response" rows="30" cols="50" readonly>$response</textarea><br>
    <label for="inp_prompt">Prompt</label><br>
    <input type="text" name="inp_prompt" id="inp_prompt" placeholder="Escribe tu prompt" required><br>
    <button type="submit" name="generar">Generar</button>
  </form>
</div>
```

Tu archivo `app.py` recibirá el prompt desde el formulario:

```python
prompt = formulario.inp_prompt
```

Se construye el diccionario para la petición a la API:

```python
data = {
    "model": "gemma3:1b",
    "prompt": prompt,
    "stream": False
}
```

Se hace la petición a Ollama:

```python
url = "http://localhost:11434/api/generate"
response = requests.post(url, json=data)
response = json.loads(response.text)
```

Se renderiza la respuesta en la página web:

```python
return render.index(response=response["response"])
```

---

## ☁️ Uso de la API de GroqCloud

También puedes usar la API de GroqCloud para generar respuestas desde la nube.

### 🔐 Requiere API Key (reemplaza `{YOUR_API_KEY}`)

```sh
curl "https://api.groq.com/openai/v1/chat/completions" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {YOUR_API_KEY}" \
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
    "stream": false
  }'
```

---

## 🐍 1. Uso desde Python

Define los headers y el cuerpo de la petición:

```python
headers = {
    "Authorization": "Bearer {YOUR_API_KEY}",
    "Content-Type": "application/json"
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
```

---

## 📡 2. Hacer la petición

```python
response = requests.post(url, headers=headers, json=data)
response = json.loads(response.text)
```

---

## 💾 3. Obtener y mostrar el mensaje

```python
print(response["choices"][0]["message"]["content"])
response = response["choices"][0]["message"]["content"]
```

---

## 🔄 4. Retornar la respuesta en el HTML

```python
return render.index(response)
```

---

## ✅ Conclusión

Este proyecto demuestra cómo:

* Ejecutar modelos de lenguaje de forma local con **Ollama**.
* Crear una **interfaz web simple** para interactuar con los modelos.
* Conectarse a la **API de GroqCloud** para generar texto desde la nube.
* Integrar fácilmente estas tecnologías en tus aplicaciones web.
