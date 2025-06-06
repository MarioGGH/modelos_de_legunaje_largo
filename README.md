# Modelos de legunaje largo

## 1. Conectarse a la api de ollama
curl http://localhost:11434/api/generate -d '{
    "model": "gemma3:1b",
    "prompt":"De que color es el cielo?"
}'