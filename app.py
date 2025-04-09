import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

csv_file_path = '/workspaces/informatica/dati.csv'

@app.route('/')
def home():
    dati = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dati.append(row)
    return render_template('index.html', dati=dati)

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    dati = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        dati = list(reader)
    
    if request.method == 'POST':
        # Aggiorna i dati con quelli inviati dal form
        dati[index]['Nome'] = request.form['Nome']
        dati[index]['Cognome'] = request.form['Cognome']
        dati[index]['Scuola'] = request.form['Scuola']
        dati[index]['Hobby'] = request.form['Hobby']
        
        # Salva i dati aggiornati nel file CSV
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Nome', 'Cognome', 'Scuola', 'Hobby']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dati)
        
        return redirect(url_for('home'))
    
    return render_template('edit.html', dato=dati[index], index=index)

if __name__ == '__main__':
    app.run(debug=True)