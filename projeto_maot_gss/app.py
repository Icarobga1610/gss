import threading
import webbrowser

from flask import Flask, render_template

from executor.base import executar_plano
from planejador import gerar_plano

app = Flask(__name__)


# Rota padrão
@app.route("/")
def index():
    return render_template("index.html")


# Rota dinâmica para execução de tipo de fraude
@app.route("/executar/<tipo>")
def executar_tipo(tipo):
    prompt_map = {
        "tipo1": "Análise de ausência de leitura",
        "tipo2": "Análise de possível vazamento",
        "tipo3": "Análise de consumo zerado com OS reincidente"
    }

    if tipo not in prompt_map:
        return render_template("404.html"), 404

    prompt = prompt_map[tipo]
    plano = gerar_plano(prompt)
    resultado = executar_plano(plano, tipo=tipo)

    return render_template("aba_analise.html", plano=plano, resultado=resultado)


# Tratamento de página não encontrada
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Abrir navegador automaticamente
def abrir_navegador():
    webbrowser.open_new("http://127.0.0.1:5050")


# Inicialização
if __name__ == "__main__":
    threading.Timer(1.0, abrir_navegador).start()
    app.run(debug=True, port=5050)
