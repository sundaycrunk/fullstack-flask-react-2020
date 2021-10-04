from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    request_method = request.method
    if request.method == "POST":
        print('#############')
        print(request.form)
        print('#############')
        return redirect(url_for(name))
    return render_template('hello.html', request_method=request_method)

@app.route('/name')
def name():
    return 'name'

@app.route('/<string:name>')
def greet(name):
    name = name.capitalize()
    return f'Hello {name}.'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
