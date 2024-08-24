from flask import Flask, render_template, request, redirect, url_for
from main import sorteio_main
import settings.setting as settings

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sorteio", methods=["POST"])
def sorteio():
    if request.method == "POST":
        #Transforma ImmutableMultiDict em List[Tuple[str, str]]
        form_data = [(key, value) for key, values in request.form.lists() for value in values]

        familia_json = {}
        key_familia_atual = None

        for familia, dado in form_data:
            if familia.endswith("_email"):
                key_familia_atual = dado.split("@")[0]
                familia_json[key_familia_atual] = {"email": dado, "familia": []}

            if familia.endswith("_membro"):
                familia_json[key_familia_atual]["familia"].append(dado)

        status = sorteio_main(familia_json)["status"]

        return redirect(url_for('resultado', status=status))

    else:
        return render_template("index.html")

@app.route("/resultado/<status>")
def resultado(status: bool):
    status = status if status == "True" else False
    msg = "Sorteio realizado com sucesso."

    if not status:
        msg = "Não foi possível realizar o sorteio. Por favor tente novamente."

    return render_template("resultado.html", message=msg)

if __name__ == '__main__':
    app.run(debug=True)