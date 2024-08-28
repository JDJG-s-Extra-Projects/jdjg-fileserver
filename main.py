import uvicorn
from fastapi import FastAPI


app = FastAPI()

# port 6234

if __name__ == "__main__":

    uvicorn.run("main:app", port=6234, log_level="debug")
