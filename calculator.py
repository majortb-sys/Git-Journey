from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("static/index.html")

@app.post("/api/calc")
async def calculate(data: dict):
    expression = data.get("expression", "")
    if not expression:
        raise HTTPException(status_code=400, detail="Expression is required")
    try:
        # Evaluate the expression safely (for demo purposes)
        result = eval(expression)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid expression: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)