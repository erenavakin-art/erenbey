import g4f
import g4f
import uvicorn
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# FastAPI'yi dahil ediyoruz

# G4F'in API nesnesini doğrudan bir içe aktarma hatası almadan almaya çalışıyoruz.
# Bunu, G4F'in kendisini bir fonksiyon olarak çağırarak yapıyoruz.
g4f_app = g4f.app.API() 

# Gerekli G4F ayarlarını yapıyoruz (Artık g4f_app üzerinden)
g4f_app.model = "llama-3-8b"
g4f_app.provider = g4f.Provider.DeepInfra

# G4F API'sini barındıracak ana FastAPI uygulamasını oluşturuyoruz
app = FastAPI()

# Çapraz Kaynak Paylaşımı (CORS) ayarları. Siteniz için KRİTİKTİR.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# G4F'in tüm yollarını (routes) ana uygulamaya dahil ediyoruz
app.include_router(g4f_app.router)

# Render'ın portunu alıyoruz
PORT = int(os.environ.get("PORT", 8080))

if __name__ == '__main__':
    # Uvicorn'ı, ana FastAPI uygulamamızı çalıştırarak başlatıyoruz
    uvicorn.run(app, host="0.0.0.0", port=PORT)
