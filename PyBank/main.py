import os
import csv

# Set path for file
csv_path = os.path.join("PyBank","Resources","budget_data.csv")

#Set up the lists to store the months and profits
months = []
profits = []
months = []
# Initialize max_value to the smallest possible integer
max_value = float('-inf')
max_index = 0
min_value = float('inf')
min_index = 0

# Open the CSV using the UTF-8 encoding
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # Add data in the months column to the months list
        months.append(row[0])
        # Add data in the profit/loss column to the profits list
        profit = int(row[1])
        profits.append(profit)
        # Update max_value and max_index if the current profit is greater than max_value
        if profit > max_value:
            max_value = profit
            max_index = len(profits) - 1
        # Update min_value and min_index if the current profit is less than min_value
        if profit < min_value:
            min_value = profit
            min_index = len(profits) - 1

#Close the file
csvfile.close()

#Initializing the max and min values for finding the greatest increase and decrease in profits:
max_diff = 0
min_diff = 0

# Initializing the total changes in profits
total_diff = 0

#Looping through the profits list:
for i in range(len(profits)-1):
    #Finding the difference in profits
    diff = profits[i+1] - profits[i]    
    #if the difference is less than the current minimum
    if diff < min_diff:
        # set the new minimum
        min_diff = diff
        # get the index of the current diff
        min_date = months[i+1]
    #if the difference is greater than the current maximum
    if diff > max_diff:
        # set the new maximum
        max_diff = diff
        # get the index of the current diff
        max_date = months[i+1]
    # add the difference to the total difference
    total_diff += diff

#find the total months
total_months = len(months)

#find the total net profit
total = sum(profits)

#find the average difference in profits
average_diff = total_diff/(total_months-1)

#find the month with the greatest increase in profits
highest_month = months[max_index]

#find the month with the greatest decrease in profits
lowest_month = months[min_index]

#Specify the file to write to
output_path = os.path.join("PyBank","analysis","results.txt")
#Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    #Write the content on to a text file
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n") 
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total}\n")
    txtfile.write(f"Average Change: ${average_diff}\n")
    txtfile.write('Greatest Increase in Profits: ' + highest_month + '($' + str(max_diff) + ') \n\n')
    txtfile.write('Greatest Decrease in Profits: ' + lowest_month +  '($' + str(min_diff) + ') \n\n')


#Open the output file in read mode
with open(output_path, 'r') as txtfile:

    #Print the contents of the text file
    print(txtfile.read())


    txtfile.write(f"Average Change: ${average_diff}\n")
    txtfile.write('Greatest Increase in Profits: ' + highest_month + '($' + str(max_diff) + ') \n\n')
    txtfile.write('Greatest Decrease in Profits: ' + lowest_month +  '($' + str(min_diff) + ') \n\n')
 

    #Close the file
    txtfile.close()

    # Open the output file in read mode

# Open the CSV using the UTF-8 encoding
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row first
    csv_header = next(csvreader)
    

    # Read each row of data after the header
    for row in csvreader:
        # Add data in the months column to the months list
        months.append(row[0])
        # Add data in the profit/loss column to the profits list
        profits.append(int(row[1]))

#Close the file
csvfile.close()

#Initializing the max and min values for finding the greatest increase and decrease in profits:
max = 0
min = 0

# Initializing the total changes in profits
total_diff = 0

#Looping through the profits list:
for i in range(len(profits)-1):
    #Finding the difference in profits
    diff = profits[i+1] - profits[i]    
    #if the difference is less than the current minimum
    if diff < min:
        # set the new minimum
        min = diff
        # get the inde of the current diff
        min_date = months[i+1]
#if the difference is greater than the current maximum
if diff > max:
    # set the new maximum
    max = diff
    # get the index of the current diff
    max_date = months[i+1]
# add the difference to the total difference
total_diff += diff

#find the total months
total_months = len(months)

#find the total net profit
total = sum(profits)

#find the average difference in profits
average_diff = total_diff/(total_months-1)

#find the month with the greatest increase in profits
highest_month = months[max_index]

#find the month with the greatest decrease in profits
lowest_month = months[min_index]

#Specify the file to write to
output_path = os.path.join("PyBank","analysis","results.txt")
#Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    #Write the content on to a text file
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n") 
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total}\n")
    txtfile.write(f"Average Change: ${average_diff}\n")
    txtfile.write('Greatest Increase in Profits: ' + highest_month + '($' + str(max) + ') \n\n')
    txtfile.write('Greatest Decrease in Profits: ' + lowest_month +  '($' + str(min) + ') \n\n')


#Open the output file in read mode
with open(output_path, 'r') as txtfile:

    #Print the contents of the text file
    print(txtfile.read())


    txtfile.write(f"Average Change: ${average_diff}\n")
    txtfile.write('Greatest Increase in Profits: ' + highest_month + '($' + str(max) + ') \n\n')
    txtfile.write('Greatest Decrease in Profits: ' + lowest_month +  '($' + str(min) + ') \n\n')
 

    #Close the file
    txtfile.close()

    # Open the output file in read mode
    with open(output_path, 'r') as txtfile:

        # Print the contents of the text file
        print(txtfile.read())

        # Close the file
        txtfile.close()






