# PyBank Assignment

# Import dependencies
import os
import csv

# Establish path
pybank_path = os.path.join("Resources", "budget_data.csv")

# Open output_file
with open(pybank_path, newline="") as csvfile:
    # Read output_file
    pybank_reader = csv.reader(csvfile, delimiter=",")

    print(pybank_reader)

    head = next(pybank_reader)
    print(f"Header: {head}")

    # Empty variables
    total_months = []
    net_pl = []
    change_pl = []

    # Append rows 
    for row in pybank_reader:
        
        total_months.append(row[0])

        net_pl.append(float(row[1]))

    # Monthly change
    for i in range(1, len(net_pl)):
        change_pl.append(float(net_pl[i] - net_pl[i-1]))

    
    print(f"Financial Analysis")

    print(f".........................................")

    print(f"Total months = {len(total_months)}")
    
    print(f"Net revenue = {sum(net_pl)}")

    print(f"Average monthly change in revenue = {sum(change_pl)/len(change_pl)}")

    print(f"Max revenue gain = [{total_months[change_pl.index(max(change_pl))]}] {float(max(change_pl))}")

    print(f"Max revenue loss = [{total_months[change_pl.index(min(change_pl))]}] {float(min(change_pl))}")


    # Output output_file
    output_file = open("pyanalysis.txt", "w")

    output_file.write(f"Financial Analysis \n")

    output_file.write(f"......................................... \n")

    output_file.write(f"Total months = {len(total_months)} \n")
    
    output_file.write(f"Net revenue = {sum(net_pl)} \n")

    output_file.write(f"Average monthly change in revenue = {sum(change_pl)/len(change_pl)} \n")

    output_file.write(f"Max revenue gain = {(total_months[change_pl.index(max(change_pl))])} {float(max(change_pl))} \n")

    output_file.write(f"Max revenue loss = {(total_months[change_pl.index(min(change_pl))])} {float(min(change_pl))} \n")

    output_file.close()