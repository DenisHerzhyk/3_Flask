from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/count', methods=['POST'])
def count():
    text = request.form["text"]
    words_count = len(text.split())
    return render_template('count.html', words_count=words_count)


if __name__ == '__main__':
    app.run(debug=True)
