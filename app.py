from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []
next_id = 1

PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
PRIORITY_LABELS = {"high": "高", "medium": "中", "low": "低"}


@app.route("/")
def index():
    sorted_todos = sorted(todos, key=lambda t: PRIORITY_ORDER[t["priority"]])
    return render_template("index.html", todos=sorted_todos, priority_labels=PRIORITY_LABELS)


@app.route("/add", methods=["POST"])
def add():
    global next_id
    content = request.form.get("content", "").strip()
    priority = request.form.get("priority", "medium")
    if priority not in PRIORITY_ORDER:
        priority = "medium"
    if content:
        todos.append({"id": next_id, "content": content, "completed": False, "priority": priority})
        next_id += 1
    return redirect(url_for("index"))


@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = not todo["completed"]
            break
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
