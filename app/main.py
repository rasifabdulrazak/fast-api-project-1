from fastapi import FastAPI


app = FastAPI(
    title="Project 1",
    description="Sample Fast API project"
)

@app.get('/')
def get_root():
    return {"index":"homepage"}