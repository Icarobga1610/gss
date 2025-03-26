import threading
import webbrowser

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def abrir_navegador():
    webbrowser.open_new('http://127.0.0.1:5050')

if __name__ == '__main__':
    threading.Timer(1.0, abrir_navegador).start()
    app.run(debug=True, port=5050)
