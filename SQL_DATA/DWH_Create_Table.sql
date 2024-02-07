DROP TABLE F_Operation;
DROP TABLE D_Date_Compta;
DROP TABLE D_Transaction;
DROP TABLE D_Type_Ope;

CREATE TABLE D_Date_Compta (
    PK_Date_Compta DATE PRIMARY KEY
);

CREATE TABLE D_Transaction (
    PK_Code CHAR(1) PRIMARY KEY
);

CREATE TABLE D_Type_Ope (
    PK_Ope VARCHAR2(150) PRIMARY KEY,
    Type VARCHAR(50),
    Categorie VARCHAR(50),
    Detail VARCHAR(50)
);

CREATE TABLE F_Operation (
    PK_Ref VARCHAR(75) PRIMARY KEY,
    FK_Date_Compta DATE,
    FK_Transaction_Code CHAR(1),
    FK_Ope VARCHAR2(150),
    Montant NUMBER(15,2),
    FOREIGN KEY (FK_Date_Compta) REFERENCES D_Date_Compta(PK_Date_Compta),
    FOREIGN KEY (FK_Transaction_Code) REFERENCES D_Transaction(PK_Code),
    FOREIGN KEY (FK_Ope) REFERENCES D_Type_Ope(PK_Ope)
);
