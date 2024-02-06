""" Creation de methode afin de repondre a :
		Quelle est la plus grosse catégorie de dépense ?
		Quelle est la plus grosse sous catégorie de source de revenue ?
		Quelles est l'évolution du solde client à travers le temps ?
"""
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import oracledb

def execute_request(query):
	"""_summary_

	Args:
		query (_type_): _description_
	"""
    try:
        connection = oracledb.connect(user='system', password='Root', host="localhost", port=1521)

        df = pd.read_sql_query(query, connection)

        connection.close()

        # Afficher les résultats dans une nouvelle fenêtre
        result_window = tk.Toplevel(root)
        result_window.title("Résultats de la requête")
        result_frame = tk.Frame(result_window)
        result_frame.pack(fill=tk.BOTH, expand=True)
        table = tk.Text(result_frame)
        table.pack(fill=tk.BOTH, expand=True)
        table.insert(tk.END, df.to_string(index=False))

    except Exception as e:
        messagebox.showerror("Erreur", str(e))


root = tk.Tk()
root.title("HB BANQUE")

# 1 - Quelle est la plus grosse catégorie de dépense ?
request = "SELECT Categorie, SUM(Montant) AS Total_Depense FROM F_Operation O JOIN D_Type_Ope T ON O.FK_Ope = T.PK_Ope WHERE FK_Transaction_Code = 'D' GROUP BY Categorie ORDER BY Total_Depense DESC FETCH FIRST ROW ONLY"
button1 = tk.Button(root, text="Requête 1", command=execute_request(request))
button1.pack()

# 2 - Quelle est la plus grosse sous-catégorie de source de revenu ?
request = "SELECT Detail, SUM(Montant) AS Total_Revenu FROM F_Operation O JOIN D_Type_Ope T ON O.FK_Ope = T.PK_Ope WHERE FK_Transaction_Code = 'C' GROUP BY Detail ORDER BY Total_Revenu DESC FETCH FIRST ROW ONLY"
button2 = tk.Button(root, text="Requête 2", command=execute_request(request))
button2.pack()

# 3 - Quelle est l’évolution du solde client à travers le temps ?
request = "SELECT fk_date_compta, Montant FROM F_Operation ORDER BY FK_Date_Compta"
button3 = tk.Button(root, text="Requête 3", command=execute_request(request))
button3.pack()

root.mainloop()
