import psycopg2
import json
from flask import Flask, render_template, request

app = Flask(__name__)


# Connection à la base de donnée avec les informations demandé.
connection = psycopg2.connect(  host= '34.95.61.235',
                                database = "stagiaires", 
                                user = "antoine.benoit-dion.1@ens.etsmtl.ca", 
                                password = "H7L5N6",
                                port = 5432)

cursor = connection.cursor()

query="SELECT score FROM score;"

cursor.execute()

results = cursor.fetchall()

#Ensuite faire des Select, pour les tables voulues.

@app.route('/', methods=['GET', 'POST'])
def number_input():
    if request.method == 'POST':
        try:
            # Récupérer la valeur de la base de donné demandé par l'utilisateur
            user_input = int(request.form['user_input'])
            if 1 <= user_input <= 100:
                return f"Excelent. Recherche dans la base de donnnées avec {user_input}" 
            else:
                return "Erreur : Veuillez saisir un nombre entre 1 et 100."
        except ValueError:
            return "Erreur : Veuillez saisir un nombre valide."        
    return render_template('number_input.html')

# Convertir les résultats en format JSON
# Exemple de données pris d'une base de données.
data = []
for row in results:
    user_data = {
        'score': row[0]
    }
    data.append(user_data)

# Formater les données en JSON
json_data = json.dumps(data, indent=2)

# Écrire le JSON dans un fichier
with open('utilisateurs.json', 'w') as file:
    file.write(json_data)

# Afficher le JSON dans la console
print(json_data)


if __name__ == '__main__':
    app.run(debug=True)
