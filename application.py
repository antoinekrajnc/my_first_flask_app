from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/urls")
def urls():
    return url_for("about")

if __name__ == "__main__":
    app.run(debug=True)
