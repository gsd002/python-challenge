#import file
import os
import csv
budget_csv=os.path.join("Resources","budget_data.csv")

#lists to store data
dates=[]
profit_loss=[]

#with open(budget_csv,encoding='utf-8') as csvfile:
with open(budget_csv) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader) #skip header
    for row in csvreader:
        #Add dates and profit_loss values to lists
        dates.append(row[0])
        profit_loss.append(float(row[1]))

        #calculate total number of months in dataset
        total_months=len(dates)

        #calculate total profit/loss for the entire period
        total_profit_loss=int(sum(profit_loss))

        #calculate changes in profit and loss and average of changes
        change=[]
        for i in range(len(profit_loss)-1):
            change.append(profit_loss[i+1]-profit_loss[i])
            avg_change=round((sum(change)/len(change)),2)
        
        #output greatest increase in profits(date and amount)
        if len(change)>0:
            greatest_increase=int(max(change))
            greatest_increase_date=dates[change.index(greatest_increase)+1]

        #output greatest decrease in profits(date and amount)
        if len(change)>0:
            greatest_decrease=int(min(change))
            greatest_decrease_date=dates[change.index(greatest_decrease)+1]

#Storing results in a dictionary
analysis_dict={"Total Months": total_months,
               "Total": total_profit_loss,
               "Average Change": avg_change,
               "Greatest Increase in Profits": {"Date": greatest_increase_date,"Amount": greatest_increase},
                "Greatest Decrease in Profits": {"Date": greatest_decrease_date, "Amount":greatest_decrease}
}

#print analysis_dict to terminal
analysis_output=(
    "Financial Analysis"
    "................................"
    f"Total Months:{analysis_dict['Total Months']}",
    f"Total:${analysis_dict['Total']}",
    f"Average Change:${analysis_dict['Average Change']}",
    f"Greatest Increase in Profits:{analysis_dict['Greatest Increase in Profits'] ['Date']}"
    f" (${analysis_dict['Greatest Increase in Profits']['Amount']})"               
        f"Greatest Decrease in Profits:{analysis_dict['Greatest Decrease in Profits'] ['Date']}"
    f" (${analysis_dict['Greatest Decrease in Profits']['Amount']})"
)

print(analysis_output)

#set variable for output file
output_file=os.path.join("Analysis","analysis.txt")
#write the ouput file
with open(output_file,"w") as file:
    file.write('\n'.join(analysis_output))
    

