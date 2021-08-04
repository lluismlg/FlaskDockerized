from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
