from flask import Flask, render_template, request, redirect
from database import (
    create_table,
    add_task,
    get_tasks,
    delete_task,
    complete_task,
    get_stats
)

app = Flask(__name__)

create_table()


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        task = request.form["task"]

        if task.strip():
            add_task(task)

        return redirect("/")

    tasks = get_tasks()

    total, completed, pending = get_stats()

    return render_template(
        "index.html",
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending
    )


@app.route("/delete/<int:task_id>")
def delete(task_id):

    delete_task(task_id)

    return redirect("/")


@app.route("/complete/<int:task_id>")
def complete(task_id):

    complete_task(task_id)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)