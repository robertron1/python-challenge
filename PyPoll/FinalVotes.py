import os
import csv
from collections import Counter
import operator

csvpath = "/Users/robertocampos/Desktop/election_data.csv"
with open(csvpath, newline='') as csvfile:   

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)				


    num_votes = []
    for row in csvreader:
        votes = row[0]
        num_votes.append(votes)
        ext_voto = len(num_votes)    
    
    print("____________________")
    print("Election Results: ")
    print("____________________")
    print("Total votes: " + str(ext_voto))

#Nombres y cantidades

csvpath = "/Users/robertocampos/Desktop/election_data.csv"
with open(csvpath, newline='') as csvfile:   
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    candidatos = []
    
    for row in csvreader:
        names = row[2]
        candidatos.append(names)
    contador = Counter(candidatos) 

    #print(contador)

    for key, value in contador.items():
        print("{}: {}".format(key, value))
        

#¿Quién tuvo más votos?

    mx = max(contador.items(), key=operator.itemgetter(1))[0]
    print("____________________")
    print("Winner: " + mx)
    
#Porcentajes:
    # total de votos: ext_voto
    # "contador" es  dictionario
    
    values = contador.values()
    total = sum(values)
    porcentaje = [value * 100. / total for value in values]
    #print(porcentaje)
    for i in range(len(porcentaje)):
        porcentaje[i] = "{:.2f}%".format(round(porcentaje[i],2))
    
    #for v in porcentaje:
        #lista_2 = v
        #print(lista_2)

    #print("Porcentages: " + str(procentaje))

#Listado 
    print("____________________")
    print("Percentages: ")
    print("____________________")

    gran_lista = []
    
    
    for p in zip (contador, porcentaje):
        #print(p)
        
        gran_lista.append("{}'s percentage: {}".format(*p))
        
    for p in gran_lista:
        print(p)

 #Exportar a .TXT   
    python FinalVotes.py > file.txt
