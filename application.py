from flask import Flask, url_for, render_template, request, make_response
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", prenom="Michel")
    elif request.method == "POST":
        nom = request.form["nom_utilisateur"]
        email = request.form["email_utilisateur"]
        message = request.form["message_utilisateur"]
        response = make_response(render_template("project.html"))
        response.set_cookies("Nom","{}".format(nom))
        return response

@app.route("/project", methods=["GET", "POST"])
def project():
    if request.method == "GET":
        return render_template("project.html")
    elif request.method == "POST":
        nom = request.form["nom_utilisateur"]
        email = request.form["email_utilisateur"]
        message = request.form["message_utilisateur"]
        return render_template("project.html", name = nom, email = email, message = message)

@app.route("/urls")
def urls():
    nom = request.cookies.get("Nom")
    return render_template("url.html", nom = nom)

if __name__ == "__main__":
    app.run(debug=True)
