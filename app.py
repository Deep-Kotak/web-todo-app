from flask import Flask, render_template, request, redirect
from database import (
    create_table,
    add_task,
    get_tasks,
    delete_task,
    complete_task,
    get_stats,
    search_tasks,
    get_task_by_id,
    update_task
)

app = Flask(__name__)

create_table()


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        task = request.form.get("task")

        if task:
            add_task(task)

        return redirect("/")

    keyword = request.args.get("search")

    if keyword:
        tasks = search_tasks(keyword)
    else:
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

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):

    if request.method == "POST":

        updated_task = request.form["task"]

        update_task(task_id, updated_task)

        return redirect("/")

    task = get_task_by_id(task_id)

    return render_template(
        "edit.html",
        task=task
    )


if __name__ == "__main__":
    app.run(debug=True)