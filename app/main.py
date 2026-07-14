from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Selamat datang di BatikAI"
    }