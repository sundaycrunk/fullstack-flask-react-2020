from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import Todo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tmp/test.db"
app.config['SECRET_KEY'] = 'password'
db = SQLAlchemy(app)

class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(240))

    def __str__(self):
        return f'{self.content}, {self.id}'

@app.route('/', methods=['GET', 'POST'])
def index():
    request_method = request.method
    if request.method == "POST":
        first_name = request.form['first_name']
        # print(request.form)
        return redirect(url_for('name', first_name=first_name))
    return render_template('hello.html', request_method=request_method)

@app.route('/name/<string:first_name>')
def name(first_name):
    return f'name = {first_name}'

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    todo_form = Todo()
    if todo_form.validate_on_submit():
        # hectic. works fine.
        print(todo_form.content.data)
        return redirect('/')
    return render_template('todo.html', form=todo_form)

@app.route('/<string:name>')
def greet(name):
    name = name.capitalize()
    return f'Hello {name}.'


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
