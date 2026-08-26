# Personal Goal Display

# Import the Keyword module
 
import keyword

#Create variables using valid python identifiers names

person_name= input("Enter your name : ")
goal_name=input("Enter your personal goal : ")
target_month=input("Enter your target month : ")
daily_minutes=int(input("Enter your daily minutes : "))

#Print multiple values together

print("\nName : ",person_name)
print("Goal : ",goal_name)
print("Target month : ",target_month)
print("Daily practice : ",daily_minutes," minutes")

#Start a new line using\n
print("\nMy personal goal plan\n")

#Change how the print statement ends
print("Goal Status ",end=":")
print("Not Started")

print("progress Reminder",end="-")
print("Practice everyday !")

# display complete goal summary

print(
    "\n",
    person_name,
    "plans to work to",
    goal_name,
    "for",
    daily_minutes,
    "minutes every day in",
    target_month," ."
)

#print python's reserved keywords

print("\nPython Keywords are ",end="-")
print(keyword.kwlist)

