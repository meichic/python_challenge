#path to csv file
budget_data = os.path.join("budget_data.csv")


total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#open and read the csv file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #reading the header row
    csv_header = next(csvreader)

    #reading the first row
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    #iterating through each row of data
    for row in csvreader:
        #keeping track of the dates
        dates.append(row[0])
        
        #calculate the change, then add to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #total number of months
        total_months += 1

        #total net amount of "Profit/Losses over entire period"
        total_pl = total_pl + int(row[1])

    #greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #greatest decrease in losses 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #average of the changes in "Profit/Losses" over the entire period
    avg_change = sum(profits)/len(profits)
    


output = (
    
    f'Financial Analysis\n'
    f'--------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total Revenue: ${total_pl}\n'
    f'Average Change: ${(round(avg_change,2))}\n'
    f'Greatest increase in Revenue: {greatest_date} ${greatest_increase}\n'
    f'Greatest decrease in Revenue: {worst_date} ${greatest_decrease}'
)

print(output)

#export results to text file
output_txt = os.path.join("output.txt")
with open(output_txt, "w") as txt_file:
    txt_file.write(output)
