from flask import Flask, render_template, request, redirect
from database import create_table, add_task, get_tasks

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

    return render_template(
        "index.html",
        tasks=tasks
    )

if __name__ == "__main__":
    app.run(debug=True)