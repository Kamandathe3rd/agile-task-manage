
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

tasks = []
next_id = 1


@app.get("/")
def home():
    return """
    <h1>Task Manager</h1>
    <form action="/tasks" method="post">
      <input name="title" placeholder="Enter a task" required>
      <button>Add Task</button>
    </form>
    <p>View tasks at <a href="/tasks">/tasks</a></p>
    """


@app.route("/tasks", methods=["GET", "POST"])
def manage_tasks():
    global next_id

    if request.method == "POST":
        data = request.get_json(silent=True) or request.form
        title = str(data.get("title", "")).strip()

        if not title:
            return jsonify({"error": "Title is required"}), 400

        task = {"id": next_id, "title": title, "done": False}
        next_id += 1
        tasks.append(task)
        app.logger.info("Task created: %s", task["id"])
        return jsonify(task), 201

    return jsonify(tasks)


@app.post("/tasks/<int:task_id>/complete")
def complete_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    task["done"] = True
    app.logger.info("Task completed: %s", task_id)
    return jsonify(task)


@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    tasks.remove(task)
    app.logger.info("Task deleted: %s", task_id)
    return jsonify({"message": "Task deleted"})


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(debug=True)
