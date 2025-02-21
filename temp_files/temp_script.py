from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return '<h1>Welcome to the Flask Web Application!</h1>'

# Greeting route with user input
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        return f'<h1>Hello, {name}!</h1>'
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            <input type="submit" value="Greet">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
