from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Todo App running on EKS 🚀"
    }

@app.get("/health")
def health():
    return {"health": "good"}
