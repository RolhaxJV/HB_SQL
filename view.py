""" Creation of a method to respond to:
        What is the biggest expense category?
        What is the largest revenue source subcategory?
        How has the customer balance changed over time?
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import oracledb
import sql_request

def execute_graf():
    """ Execute a predefined SQL query and display the result as a Cartesian graph """
    try:
        connection = oracledb.connect(user='system', password='Root', host="localhost", port=1521)
        cursor = connection.cursor()

        cursor.execute(sql_request.customer_balance())
        rows = cursor.fetchall()

        fig = Figure(figsize=(8, 6))
        ax = fig.add_subplot(111)

        dates = [row[0] for row in rows]
        montants = [row[1] for row in rows]

        ax.plot(dates, montants, marker='o', linestyle='-')

        ax.set_title('Montant en fonction de la date')
        ax.set_xlabel('Date')
        ax.set_ylabel('Montant')

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        cursor.close()
        connection.close()

    except Exception as e:
        messagebox.showerror("Erreur", str(e))

def execute_request(query):
    """ Execute the sql request pass in parameter

    Args:
        query (str): request sql
    """
    try:
        connection = oracledb.connect(user='system', password='Root', host="localhost", port=1521)

        df = pd.read_sql_query(query, connection)

        connection.close()

        result_window = tk.Toplevel(root)
        result_window.title("Résultats de la requête")

        tree = ttk.Treeview(result_window, columns=df.columns.to_list(), show="headings")

        for col in df.columns:
            tree.heading(col, text=col)

        for index, row in df.iterrows():
            tree.insert("", "end", values=row.tolist())

        tree.pack(fill="both", expand=True)

    except Exception as e:
        messagebox.showerror("Erreur", str(e))

root = tk.Tk()
root.title("HB BANQUE")

# 1 - What is the biggest expense category?
button1 = tk.Button(root, text="Requête 1", command=lambda: execute_request(sql_request.biggest_expense()))
button1.pack()

# 2 - What is the largest income source subcategory?
button2 = tk.Button(root, text="Requête 2", command=lambda: execute_request(sql_request.largest_income()))
button2.pack()

# 3 - How has the customer balance changed over time?
button3 = tk.Button(root, text="Requête 3", command=execute_graf)
button3.pack()

root.mainloop()
