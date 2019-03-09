import os
import csv
csvpath = "/Users/robertocampos/Desktop/budget_data.csv"
with open(csvpath, newline='') as csvfile:   

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)				


#NUMBER OF MONTHS

    num_months = []
    for row in csvreader:
        months = row[0]

        num_months.append(months)
    ext_month = len(num_months)  
    
    print("Financial Analysis")
    print("----------------------------")  
    print("Number of months: " + str(ext_month))
				

#TOTAL

csvpath = "/Users/robertocampos/Desktop/budget_data.csv"
with open(csvpath, newline='') as csvfile:   

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)				
    

    profit_losses_list = []
    
    for row in csvreader:
        amount = row[1]

        profit_losses_list.append(amount)
    
    profit_losses_list = [int(i) for i in profit_losses_list]
    
    sum_numbers = sum(profit_losses_list)

    print("Total: " + str(sum_numbers))
   
# AVERAGE

csvpath = "/Users/robertocampos/Desktop/budget_data.csv"
with open(csvpath, newline='') as csvfile:   

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)				
  
    

    cifras = []
    
    for row in csvreader:
        amount = row[1]
        cifras.append(amount)

    cifras = [int(i) for i in cifras] 
    
    b = []
    for i in range(1, len(cifras)):
        a = ((cifras[i]-cifras[i-1]))
        b.append(a)
    m = sum(b) / float(len(b))
    
    print("Average Change: " + str(m))

# GIP & GDP:

csvpath = "/Users/robertocampos/Desktop/budget_data.csv"
with open(csvpath, newline='') as csvfile:   

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)				
    
    

    cifras = []
    
    for row in csvreader:
        amount = row[1]
        cifras.append(amount)

    cifras = [int(i) for i in cifras] 
    
b = []
for i in range(1, len(cifras)):
    a = ((cifras[i]-cifras[i-1]))
    b.append(a)

GIP = max(b)
GDP = min(b)

print("Greatest Increase in Profits: $" + str(GIP))
print("Greatest Decrease in Profits: $" + str(GDP))


# GUARDAR DOCUMENTO

    # En la consola: python fin.py > file.txt
