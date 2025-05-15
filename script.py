from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Banco:
    sistema = []

    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self._ativo = True

    def __str__(self):
        return f'{self.titular} - Saldo: {self.saldo} - Limite: {self.limite} - Ativo: {self._ativo}'

    @classmethod
    def listar_contas(cls):
        return cls.sistema


@app.route("/", methods=["GET", "POST"])
def cadastro_clientes():
    if request.method == "POST":
        nome = request.form['nome']
        saldo = request.form['saldo']
        limite = request.form['limite']

        cliente = Banco(nome, saldo, limite)
        Banco.sistema.append(cliente)
    return render_template("home.html")


@app.route("/listar-clientes", methods=["GET"])
def listar_clientes():
    clientes = Banco.listar_contas()
    return render_template("listar_cliente.html", clientes=clientes)

@app.route("/delete-cliente", methods=["POST"])
def deletar_cliente():
    index = int(request.form["index"])
    if 0 <= index < len(Banco.sistema):
        deletado = Banco.sistema.pop(index)
        print(f"Cliente {deletado.titular} deletado")
    return redirect("/listar-clientes")


if __name__ == "__main__":
    app.run(debug=True)
