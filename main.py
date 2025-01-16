from fastapi import FastAPI, Request
import uvicorn

# Create FastAPI app
app = FastAPI()

@app.get("/")
async def read_root():
    print("GET done")
    return {"message": "GET request received"}

@app.post("/")
async def create_item(request: Request):
    print("POST done")
    data = await request.json()
    return {"message": "POST request received", "data": data}

if __name__ == "__main__":
    # Run the Uvicorn server
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)