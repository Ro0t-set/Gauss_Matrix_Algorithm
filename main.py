import numpy as np
from fractions import Fraction

##########now only works with square matrices############

class Matritce():
    def __init__(self, matrice, risultati, row, column):
        self.matrice = matrice
        self.risultati = risultati
        self.row = row
        self.column = column

    def PrintMareix(self):
        print(self.matrice,"\n results: ",self.risultati, "\n\n")

    def forse_mi_serve___testing____(self):
        for matriceX in self.matrice:
            print('\n- - - - - - - - - - - - - -')
            for numero in matriceX:
                numero = Fraction(str(numero))
                print(numero, end="      ")




    def InserisciDati(self):
        R = int(input("Enter the number of rows:"))
        C = int(input("Enter the number of columns:"))

        print("Enter the matrice in a single line (separated by space): ")

        # User input of entries in a
        # single line separated by space
        matrice = list(map(int, input().split()))
        print("Enter the risulatai in a single line (separated by space): ")
        risultati = list(map(int, input().split()))

        # For printing the matrix
        self.matrice = np.array(matrice, float).reshape(R, C)
        self.risultati = np.array(risultati, float).reshape(C)
        self.column = C
        self.row = R
        print("Inserted Matrix:")
        self.PrintMareix(self)

    def MakeScala(self):
        k=0
        for i in range(0, (self.row)-1):
            numeratore = self.matrice[i,k] # diagonal selection
            k = k + 1
            for j in range(k, (self.row)):
                denominatore = self.matrice[j, i]
                if(denominatore==0  or numeratore==0): break
                self.risultati[j] = self.risultati[j]*(numeratore/denominatore)
                self.risultati[j] = self.risultati[i] - self.risultati[j]
                for r in range(0, self.column):
                    self.matrice[j, r] =  ( self.matrice[j, r] * (numeratore/denominatore))
                    self.matrice[j , r] =  self.matrice[i,r] - self.matrice[j, r]
        print("OUTPUT:")
        self.PrintMareix(self)


#Testing
# matrice=([3,-2,5,0],
#          [4,5,8,1],
#          [1,1,2,1],
#          [2,7,6,5])
# Matritce.matrice= np.array(matrice, float)
# Matritce.risultati=[2,4,5,7]
# Matritce.row= 4
# Matritce.column=4
# Matritce.PrintMareix(Matritce)

# 1 -1 0 1 2 0 0 6 -4

Matritce.InserisciDati(Matritce)
Matritce.MakeScala(Matritce)
