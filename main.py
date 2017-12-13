from flask import *
import knownartist as ka
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/checkCred", methods=["POST"])
def checkCred():
    username = request.form['username_form']
    password = request.form['password_form']
    if artist == other:
        pass
    else:
        status = ka.checkcreddb(artist)
    if status == 1:
        return redirect(url_for("displayHome"))
    else:
        return redirect(url_for("main"))

@app.route("/displayRegister")
def displayRegister():
    return render_template("register.html")


if __name__ == "__main__":
    app.run()
