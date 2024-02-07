-- Insertion dans Date_Compta
INSERT INTO D_Date_Compta (PK_Date_Compta)
SELECT DISTINCT TO_DATE(DATE_COMPTA, 'DD/MM/YYYY') FROM ODS_BANQUE;

-- Insertion dans Transaction
INSERT INTO D_Transaction (PK_Code) VALUES ('D');
INSERT INTO D_Transaction (PK_Code) VALUES ('C');

-- Insertion dans Type_Ope
INSERT INTO D_Type_Ope (PK_Ope,Type, Categorie, Detail)
SELECT DISTINCT T_OPE || CATEGORIE || S_CATE AS FK_Ope, T_OPE, CATEGORIE, S_CATE 
FROM ODS_BANQUE;

-- Insertion dans Operation
INSERT INTO F_Operation (PK_Ref, FK_Date_Compta, FK_Transaction_Code, FK_Ope, Montant)
SELECT
    REF,
    TO_DATE(DATE_COMPTA, 'DD/MM/YYYY'),
    Transaction_Code,
    FK_Ope,
    TO_NUMBER(Montant)
FROM (
    SELECT
        REF,
        DATE_COMPTA,
        'D' AS Transaction_Code,
        T_OPE || CATEGORIE || S_CATE AS FK_Ope,
        DEBIT AS Montant -- CASE == 0 PASS
    FROM ODS_BANQUE
    WHERE DEBIT != 0 
    UNION ALL
    SELECT
        REF,
        DATE_COMPTA,
        'C' AS Transaction_Code,
        T_OPE || CATEGORIE || S_CATE AS FK_Ope,
        CREDIT AS Montant
    FROM ODS_BANQUE
    WHERE CREDIT != 0
    ) UNITES_TABLES;
