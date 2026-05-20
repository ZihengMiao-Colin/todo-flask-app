from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []
next_id = 1


@app.route("/")
def index():
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    global next_id
    content = request.form.get("content", "").strip()
    if content:
        todos.append({"id": next_id, "content": content, "completed": False})
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
