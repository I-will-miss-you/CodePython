from flask import Flask, render_template, redirect, url_for, request

from student import Student

students = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def students_page():
    if request.method == "POST":
        new_student_id = request.form.get("student-id", "")
        new_student_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")
        request_type = request.form.get("type", "")

        new_student = Student(
            name=new_student_name,
            last_name=new_student_last_name,
            student_id=new_student_id)

        if(request_type == "remove"):
            students.clear()
        else:
            students.append(new_student)

        return redirect(url_for("students_page"))

    return render_template("home.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
