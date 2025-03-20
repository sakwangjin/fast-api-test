from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI Test Project",
    description="A sample FastAPI project with basic CRUD operations",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Test Project"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)