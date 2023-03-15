import random

from random import *
import csv
from datetime import *
from datetime import datetime
import time
import string
import secrets
import requests



intervalle = 99999
total = 0
total_essais = []
total_prix = []
while total <= 9999:
    total = total + 1
    chiffres = string.digits
    prix = int(''.join(secrets.choice(chiffres) for i in range(len(str(intervalle)))))
    print (prix)
    total_prix.append(prix)
    inputprix = 0
    essais = 0
    tentative = randint(0, intervalle)
    plus = []
    moins = []
    print (plus)
    print (moins)
    while (tentative) != (prix):
        essais = essais + 1

        #inputprix = int(input("Entrez un prix : "))
        print (tentative)
        if tentative < prix:
            plus.append(tentative)
            print ("C'est plus ! ")


            if len(moins) != 0 and len(plus) != 0:
                tentative = randint(max(plus), min(moins))
            else:
                tentative = randint(0, intervalle)
        
        elif tentative > prix:
            moins.append(tentative)
            print ("C'est moins ! ")
            if len(moins) != 0 and len(plus) != 0:
                tentative = round(int(uniform(max(plus), min(moins))))
            else:
                tentative = round(int(uniform(0, intervalle)))
            

  
    total_essais.append(essais)
 


values = (f"intervalle : {int(intervalle)}, moyenne prix : {int(sum(total_prix)/len(total_essais))}, exécutions : {len(total_essais)}, moyenne essais : {(sum(total_essais)/len(total_essais))}")
print (values)








