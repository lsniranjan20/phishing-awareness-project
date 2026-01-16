from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        print("DUMMY DATA RECEIVED (Awareness Demo)")
        print("Username:", username)
        print("Password:", password)

        return "Login failed! (This is a phishing awareness demo)"

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


