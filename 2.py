#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator: ")
#Total bill: 150
bill=int(input("What was the total bill? \n"))
tip=int(input("What percentage tip would you like to give? \n"))
people=int(input("How many people to split the bill? \n"))
tip_as_percent= tip / 100
total_tip_ammount= bill * tip_as_percent 
total_bill=bill+total_tip_ammount
split_total=total_bill / people
final_amount="{:.2f}".format(split_total)
print(f"Each person should pay: \n ${final_amount}")