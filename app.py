import g4f
import uvicorn
import os
# En güncel sürümde bu import'un çalışması GEREKİR.
from g4f.api import api as g4f_app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# G4F API'sini barındıracak ana FastAPI uygulamasını oluşturuyoruz
app = FastAPI()

# Çapraz Kaynak Paylaşımı (CORS) ayarları.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# G4F'in tüm yollarını (routes) ana uygulamaya dahil ediyoruz
app.include_router(g4f_app.router)

# Gerekli G4F ayarlarını yapıyoruz 
g4f_app.model = "llama-3-8b"
g4f_app.provider = g4f.Provider.DeepInfra

# Render'ın portunu alıyoruz
PORT = int(os.environ.get("PORT", 8080))

if __name__ == '__main__':
    # Uvicorn'ı, ana FastAPI uygulamamızı çalıştırarak başlatıyoruz
    uvicorn.run(app, host="0.0.0.0", port=PORT)
