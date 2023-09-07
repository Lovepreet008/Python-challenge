import os
import csv

budgetcsv= os.path.join("Resources", "budget_data.csv")

with open(budgetcsv,'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)
    count=0
    total_sum=0
    previous_entry=0
    change_list=[]
    Max_num=99999999999
    Min_num=0
    greatest_dec=["",0]
    greatest_Inc=["",0]
    


    for row in csvreader:
        #count number of months
        count+=1
        #total sum
        total_sum= total_sum+int(row[1])
        #calculate the difference and add to list
        if previous_entry!=0:
            changes=int(row[1])-previous_entry
            
            change_list.append(changes)
        
        # calculate the greatest decrease in profit

            if changes< Max_num:
                greatest_dec[0]=row[0]
                greatest_dec[1]=changes
                Max_num=changes
            # calculate the greatest increase in profit
            if changes> Min_num:
                greatest_Inc[0]=row[0]
                greatest_Inc[1]=changes
                Min_num=changes
        previous_entry=int(row[1])

    




    print("Finacial Analysis")
    print("_____________________________")
    print("                             ")
    #Display months
    print(f'Total months: {count}')
    print("                             ")
    #Display total sum
    print(f'Total: ${total_sum}')
    print("                             ")
    #Calculate and print average
    Average= float((sum(change_list))/ len(change_list))
    print(f'Average Change: ${round(Average,2)}')
    print("                             ")
    #print greatest increase
    print(f'Greatest Increase in Profits: {greatest_Inc[0]} (${ greatest_Inc[1]})')
    print("                             ")
    #print greatest decrease
    print(f'Greatest Decrease in Profits: {greatest_dec[0]} (${ greatest_dec[1]})')
    #$-8311.11






