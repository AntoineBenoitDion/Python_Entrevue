#import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def number_input():
    if request.method == 'POST':
        try:
            # Récupérer la vlaeur de la base de donné demandé par l'utilisateur
            user_input = int(request.form['user_input'])
            if 1 <= user_input <= 100:
                return f"Excelent. Recherche dans la base de donnnées avec {user_input}"   
            else:
                return "Erreur : Veuillez saisir un nombre entre 1 et 100."
        except ValueError:
            return "Erreur : Veuillez saisir un nombre valide."        
    return render_template('number_input.html')

if __name__ == '__main__':
    app.run(debug=True)

# Connection à la base de donnée avec les informations demandé.
#conn = psycopg2.connect(database = "stagiaires", 
#                        user = "antoine.benoit-dion.1@ens.etsmtl.ca", 
#                        host= '34.95.61.235',
#                        password = "H7L5N6",
#                        port = 5432)

