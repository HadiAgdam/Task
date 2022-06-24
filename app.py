from flask import Flask, request, render_template

app = Flask(__name__)

# test

@app.route('/')
def hello_world():
    return render_template('home/index.html')


if __name__ == '__main__':
    app.run()
