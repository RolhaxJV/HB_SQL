""" Requete sql utiliser dans la view """

def biggest_expense():
    return "SELECT Categorie, SUM(Montant) AS Total_Depense FROM F_Operation O JOIN D_Type_Ope T ON O.FK_Ope = T.PK_Ope WHERE FK_Transaction_Code = 'D' GROUP BY Categorie ORDER BY Total_Depense FETCH FIRST ROW ONLY"

def largest_income():
    return "SELECT Detail, SUM(Montant) AS Total_Revenu FROM F_Operation O JOIN D_Type_Ope T ON O.FK_Ope = T.PK_Ope WHERE FK_Transaction_Code = 'C' GROUP BY Detail ORDER BY Total_Revenu DESC FETCH FIRST ROW ONLY"

def customer_balance():
    return "SELECT fk_date_compta, Montant FROM F_Operation ORDER BY FK_Date_Compta"
