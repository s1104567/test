from typing import Optional

from fastapi import FastAPI

app = FastAPI()  # 建立一个 FastAPI application



@app.get("/information/{student_id}/{name}")  # 指定 API 路径 (GET 方法)
def get_information(student_id: int, name: str):
   
    return {"Student ID": student_id, "Name": name}