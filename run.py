import uvicorn
#  uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8001, reload=True)


# asd
