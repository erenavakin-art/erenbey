import g4f
import uvicorn
from g4f.api import server
import os

# Render'ın atadığı port numarasını alıyoruz (genellikle 10000 civarıdır)
PORT = int(os.environ.get("PORT", 8080))

# API ayarlarını burada zorluyoruz (Sadece stabil olan modeli kullanması için)
app.model = "llama-3-8b"
app.provider = g4f.Provider.DeepInfra

if __name__ == '__main__':
    # Uvicorn'ı, Render'ın atadığı porta bağlayarak çalıştırıyoruz.
    uvicorn.run(app, host="0.0.0.0", port=PORT)
