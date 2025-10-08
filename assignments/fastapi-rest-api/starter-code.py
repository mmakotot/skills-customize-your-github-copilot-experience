from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = []

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: dict):
    task_id = len(tasks) + 1
    task["id"] = task_id
    tasks.append(task)
    return task

@app.delete("/tasks/{id}")
def delete_task(id: int):
    for i, task in enumerate(tasks):
        if task["id"] == id:
            del tasks[i]
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
