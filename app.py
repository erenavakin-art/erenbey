import g4f
import uvicorn
import os
from g4f.api import app as g4f_app # API nesnesini 'g4f_app' olarak yeniden adlandırıyoruz
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# G4F API'sini barındıracak ana FastAPI uygulamasını oluşturuyoruz
app = FastAPI()

# Çapraz Kaynak Paylaşımı (CORS) ayarları. Bu, sitenizin (depremdurum.ct.ws) API'yi kullanması için KRİTİKTİR.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Tüm alan adlarından gelen isteklere izin ver (Siteniz için gerekli)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# G4F'in tüm yollarını (routes) ana uygulamaya dahil ediyoruz
app.include_router(g4f_app.router)

# Gerekli G4F ayarlarını yapıyoruz (Artık g4f_app üzerinden)
g4f_app.model = "llama-3-8b"
g4f_app.provider = g4f.Provider.DeepInfra

# Render'ın portunu alıyoruz
PORT = int(os.environ.get("PORT", 8080))

if __name__ == '__main__':
    # Uvicorn'ı, ana FastAPI uygulamamızı çalıştırarak başlatıyoruz
    uvicorn.run(app, host="0.0.0.0", port=PORT)
