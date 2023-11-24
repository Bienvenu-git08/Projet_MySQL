import mysql.connector
def create_table_and_insert_data():
    try:
        # Établir la connexion à la base de données
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='school')
 
        if conn.is_connected():
            print("Connected successfully")
 
            # Partie ajoutée pour créer la table 'employee' s'il n'existe pas déjà
            create_employee = """CREATE TABLE IF NOT EXISTS employee (
                Id int(11) NOT NULL,
                Name varchar(250) NOT NULL,
                Dept varchar(50) NOT NULL,
                Age int(11) NOT NULL,
                Contact varchar(250) NOT NULL,
                PRIMARY KEY (Id)
            )"""
 
            cursor = conn.cursor()
            cursor.execute(create_employee)
            print("Table 'employee' created or already exists")
 
            # Partie ajoutée pour insérer des données dans la table 'employee'
            insert_employee = """INSERT INTO employee (Id, Name, Dept, Age, Contact)
                                 VALUES (103, 'NouveauNom', 'NouveauDept', 25, '06678338'),
                                        (104, 'AutreNom', 'AutreDept', 28, '06987224'),
                                        (105, 'jeremie', 'AutreDept', 50, '06234098'),
                                        (106, 'marc', 'NouveauDept', 38, '06704560'),
                                        (107, 'jean', 'AutreDept', 62, '06453298'),
                                        (108, 'remi', 'AutreDept', 43, '06122378'),
                                        (109, 'xavier', 'NouveauDept', 50, '06890954')"""
 
            # Vérifier si l'ID existe déjà avant d'insérer
            cursor.execute("SELECT Id FROM employee WHERE Id IN (103, 104)")
            existing_ids = {row[0] for row in cursor.fetchall()}
 
            new_entries = [(103, 'NouveauNom', 'NouveauDept', 25, '06678338'),
                           (104, 'AutreNom', 'AutreDept', 28, '06987224'),
                           (105, 'jeremie', 'AutreDept', 50, '06234098'),
                           (106, 'marc', 'NouveauDept', 38, '06704560'),
                           (107, 'jean', 'AutreDept', 62, '06453298'),
                           (108, 'remi', 'AutreDept', 43, '06122378'),
                           (109, 'xavier', 'NouveauDept', 50, '06890954')]
 
            entries_to_insert = [entry for entry in new_entries if entry[0] not in existing_ids]
 
            if entries_to_insert:
                cursor.executemany("INSERT INTO employee (Id, Name, Dept, Age, Contact) VALUES (%s, %s, %s, %s, %s)", entries_to_insert)
                conn.commit()
                print("Data inserted into 'employee' successfully")
            else:
                print("No new data to insert")
 
        else:
            print("Connection not established")
 
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
 
    finally:
        # Fermer la connexion dans tous les cas
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed")
 
def select_data():
    try:
        # Établir la connexion à la base de données
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='school')
 
        if conn.is_connected():
            print("Connected successfully")
 
            # Partie ajoutée pour sélectionner des données dans la table 'employee'
            select_employee = "SELECT * FROM employee"
 
            cursor = conn.cursor()
            cursor.execute(select_employee)
 
            result = cursor.fetchall()
 
            print("Total number of rows selected", cursor.rowcount)
            print("\nSelected data are -")
 
            for row in result:
                print("Id: ", row[0])
                print("Name: ", row[1])
                print("Dept: ", row[2])
                print("Age: ", row[3])
                print("Contact: ", row[4])
 
        else:
            print("Connection not established")
 
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
 
    finally:
        # Fermer la connexion dans tous les cas
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed")
 
def update_data():
    try:
        # Établir la connexion à la base de données
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='school')
 
        if conn.is_connected():
            print("Connected successfully")
 
            # Créer un objet curseur
            cursor = conn.cursor()
 
            # Partie ajoutée pour mettre à jour des données dans la table 'employee'
            update_employee = """UPDATE employee SET Contact='9232894873' WHERE Id = 102"""
 
            cursor.execute(update_employee)
            conn.commit()
            print("Data updated successfully.")
 
            # Partie ajoutée pour sélectionner des données dans la table 'employee' après la mise à jour
            select_employee = "SELECT * FROM employee WHERE Id = 102"
 
            cursor.execute(select_employee)
            result = cursor.fetchone()
 
            print(result)
 
        else:
            print("Connection not established")
 
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
 
    finally:
        # Fermer la connexion dans tous les cas
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed")
 
def delete_data():
    try:
        # Établir la connexion à la base de données
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='school')
 
        if conn.is_connected():
            print("Connected successfully")
 
            # Créer un objet curseur
            cursor = conn.cursor()
 
            # Partie ajoutée pour supprimer des données dans la table 'employee'
            delete_employee = """DELETE FROM employee WHERE Id = (SELECT Id FROM employee LIMIT 1)"""
 
            cursor.execute(delete_employee)
            conn.commit()
            print("Data deleted successfully.")
 
        else:
            print("Connection not established")
 
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
 
    finally:
        # Fermer la connexion dans tous les cas
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed")
 
def search_data(keyword):
    try:
        # Établir la connexion à la base de données
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='school')
 
        if conn.is_connected():
            print("Connected successfully")
 
            # Créer un objet curseur
            cursor = conn.cursor()
 
            # Partie ajoutée pour rechercher des données dans la table 'employee' par mot-clé
            search_employee = f"SELECT * FROM employee WHERE Name LIKE '%{keyword}%' OR Dept LIKE '%{keyword}%' OR Contact LIKE '%{keyword}%'"
 
            cursor.execute(search_employee)
            result = cursor.fetchall()
 
            if cursor.rowcount == 0:
                print(f"No results found for keyword '{keyword}'")
            else:
                print("\nSearch results for keyword '{}':".format(keyword))
                print("Total number of rows selected", cursor.rowcount)
                print("\nSelected data are -")
 
                for row in result:
                    print("Id: ", row[0])
                    print("Name: ", row[1])
                    print("Dept: ", row[2])
                    print("Age: ", row[3])
                    print("Contact: ", row[4])
 
        else:
            print("Connection not established")
 
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
 
    finally:
        # Fermer la connexion dans tous les cas
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Connection closed")
 
# Appeler la fonction pour créer la table et insérer des données
create_table_and_insert_data()
 
# Appeler la fonction pour sélectionner et afficher des données
select_data()
 
# Appeler la fonction pour mettre à jour des données
update_data()
 
# Appeler la fonction pour supprimer des données
delete_data()
 
# Appeler la fonction pour rechercher des données par mot-clé (par exemple, 'NouveauNom')
search_data('jeremie')
 