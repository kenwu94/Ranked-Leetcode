from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Code(BaseModel):
    language: str
    code: str

@app.post("/execute")
async def execute_code(code: Code):
    if code.language != "python":
        raise HTTPException(status_code=400, detail="Only Python is supported")
    try:
        result = subprocess.run(
            ["python", "-c", code.code],
            capture_output=True,
            text=True,
            timeout=5
        )
        return {"output": result.stdout, "error": result.stderr}
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=400, detail="Code execution timed out")
    