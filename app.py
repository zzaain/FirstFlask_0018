from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None

    if request.method == "POST":
        # Parsing parameter dari TextField menggunakan method POST
        hasil = request.form.get("teks", "").strip()

    return render_template("index.html", hasil=hasil)


if __name__ == "__main__":
    app.run(debug=True)
