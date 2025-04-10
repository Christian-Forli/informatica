from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

# Inizializza l'app Flask
app = Flask(__name__)

# Rotta principale
@app.route('/')
def home():
    # Legge i dati dal file CSV
    df = pd.read_csv('09-04-25/profilo.csv')
    dizionario = df.iloc[0].to_dict()  # Prende il primo record come dizionario
    nome = dizionario.get('Nome')  # Usa i nomi delle colonne corretti
    cognome = dizionario.get('Cognome')
    scuola = dizionario.get('Scuola')
    hobby = dizionario.get('Hobby')
    return render_template('index.html', nome=nome, cognome=cognome, scuola=scuola, hobby=hobby)

# Rotta per modificare i dati
@app.route('/modifica', methods=['GET', 'POST'])
def modifica():
    if request.method == 'POST':
        # Prende i dati dal form e li salva nel CSV
        nuovo_profilo = {
            "Nome": request.form['nome'],
            "Cognome": request.form['cognome'],
            "Scuola": request.form['scuola'],
            "Hobby": request.form['hobby']
        }
        df = pd.DataFrame([nuovo_profilo])  # Crea un DataFrame con i nuovi dati
        df.to_csv('09-04-25/profilo.csv', index=False)  # Salva nel file CSV
        return redirect(url_for('home'))  # Reindirizza alla pagina principale
    # Legge i dati esistenti dal CSV
    df = pd.read_csv('09-04-25/profilo.csv')
    dizionario = df.iloc[0].to_dict()  # Prende il primo record come dizionario
    return render_template('modifica.html', dati=dizionario)

# Avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)