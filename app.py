from flask import Flask, render_template
#render_template i import ediyoruz.
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
#tml kodlarının yazılı olduğu index.html dosyasını belirterek fonksyounumu doldurdum ve sayfamı tamamlamış oldum.


if __name__ == "__main__":
    app.run(debug=True)