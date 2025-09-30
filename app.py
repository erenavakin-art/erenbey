import g4f
import uvicorn
# KESİNLİKLE BU ŞEKİLDE OLMALI
from g4f import g4f_api 
import os

PORT = int(os.environ.get("PORT", 8080))

# Artık 'g4f_api' nesnesini kullanıyoruz
g4f_api.model = "llama-3-8b"
g4f_api.provider = g4f.Provider.DeepInfra

if __name__ == '__main__':
    # 'g4f_api' nesnesini çalıştırıyoruz
    uvicorn.run(g4f_api, host="0.0.0.0", port=PORT)
