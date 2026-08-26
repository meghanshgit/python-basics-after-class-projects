#classroom points calculator

# calculating this week points

team_blue=int(input("enter the points of blue team : "))
team_red=int(input("enter the points of red team : "))
team_orange=int(input("enter the points of orange team : "))
team_pink=int(input("enter the points of pink team : "))
team_yellow=int(input("enter the points of yellow team : "))

#calculating the total and average

total=team_blue+team_red+team_pink+team_orange+team_yellow
average=total/5

print("total points are : ",total)
print("average of points are : ",average)

#calculating reward stars

stars_per_point=2
reward_stars=total*stars_per_point

print("total reward stars are : ",reward_stars)

#calculating full packed boxes of stars and leftover stars

total_boxes=total//25
leftover=total%25

print("full packed boxes : ",total_boxes)
print("leftover stars : ",leftover)

#comparing last week's points to this week's points

last_week=int(input("enter last week's total points"))

if last_week > total:
    print("done better than last week")
elif last_week == total:
    print("donr same as last week")
else:
    print("done least than last week")

#adding bonus challenge points

bonus=30
total+=bonus

print("total points after bonus points",total)

#subtracting missed task points

missed=15
total-=missed

print("total points after missed challanges points",total)

#final star boxes count

reward_stars=total*stars_per_point
boxes=reward_stars//25

print("final boxes packed : ",boxes)