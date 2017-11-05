from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello there!"

@app.route('/square/<int:n>')
def square(n):
    return (" Square of {} = {}".format(n, n*n))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
