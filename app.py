from flask import Flask, request, render_template_string, redirect, url_for
from university import University

app = Flask(__name__)
db = University()

form_template = """
<!doctype html>
<title>Университет</title>
<h2>Управление студентами</h2>
<form method="post" action="/insert">
  <h3>Добавить студента</h3>
  ID: <input name="id" type="number" required><br>
  Имя: <input name="name" required><br>
  Возраст: <input name="age" type="number" required><br>
  Оценка: <input name="grade" type="number" required><br>
  <input type="submit" value="Добавить">
</form>

<hr>

<a href="/list">Список всех студентов</a>
"""

list_template = """
<!doctype html>
<title>Список студентов</title>
<h2>Студенты</h2>
<table border=1>
  <tr><th>ID</th><th>Имя</th><th>Возраст</th><th>Оценка</th></tr>
  {% for s in students %}
  <tr>
    <td>{{ s[0] }}</td>
    <td>{{ s[1] }}</td>
    <td>{{ s[2] }}</td>
    <td>{{ s[3] }}</td>
  </tr>
  {% endfor %}
</table>
<br>
<a href="/">Вернуться назад</a>
"""

@app.route("/", methods=["GET"])
def main_page():
    return render_template_string(form_template)

@app.route("/insert", methods=["POST"])
def insert_student():
    id = int(request.form["id"])
    name = request.form["name"]
    age = int(request.form["age"])
    grade = int(request.form["grade"])
    db.insert(id, name, age, grade)
    return redirect(url_for('list_students'))

@app.route("/list", methods=["GET"])
def list_students():
    students = db.read()
    return render_template_string(list_template, students=students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
