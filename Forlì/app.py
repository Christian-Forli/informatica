from flask import Flask,render_template #importiamo la classe flask
app = Flask(__name__) #inizializza app flask
x = "ciao"
lista = ["mele", "latte", "uova", "pasta", "creali"]


@app.route("/")
def home():
    return render_template("index.html", x = x)

#avvio flask
if __name__ == '__main__':
    app.run(debug=True) #aggiornamenti in tempo reale