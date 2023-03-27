from flask import Flask, request, render_template
from quoters import Quote

app = Flask(__name__)

@app.route('/generate_quotes')
def generate_quotes():
    return Quote.print()

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    # return f'Hello, {name}!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
