from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'secret'

@app.route("/", methods=['GET'])
def addCount():
    if "counter" not in session:
        session["counter"] = 0
    else:
        session["counter"] += 1
    return render_template("index.html")

@app.route("/addtwo", methods =['GET'])
def addtwomore():
    session["counter"] += 1
    return redirect('/')

@app.route("/destroy_session")
def countOne():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run( debug = True )