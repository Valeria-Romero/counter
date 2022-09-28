from flask import Flask, render_template, session, redirect, request

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

@app.route("/add/number", methods=['POST'])
def count_numb():
    numero = int(request.form['cantidad'])
    session["counter"] += (numero-1) #Aquí hacemos numero - 1 porque al momento de hacer el redirect se suma uno de todas formas
    return redirect("/")

if __name__ == "__main__":
    app.run( debug = True )
    