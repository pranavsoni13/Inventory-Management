from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models, database
from routes import product, auth

app = FastAPI(
    title="Inventory Management API",
    version="1.0.0"
)

origins = [
    "http://localhost:3000",
    "https://your-app.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB create
models.Base.metadata.create_all(bind=database.engine)

# Routes
app.include_router(product.router, prefix="/products", tags=["Products"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

@app.get("/")
def home():
    return {"message": "Inventory API Running 🚀"}

@app.get("/health")
def health():
    return {"status": "OK"}