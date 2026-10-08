print("==== Grocery Cost Comparision Tool ====")

 #part 1 - weeks shop's cost per person

rice_price=int(input("Enter the price of rice : "))
milk_price=int(input("Enter the price of milk : "))
fruit_price=int(input("Enter the price of fruit : "))
baskets_number=int(input("enter number of baskets : "))
family_member=int(input("Enter number of family members : "))

basket_price=rice_price+milk_price+fruit_price
total_basket_price=basket_price*baskets_number
basket_cost_per_person=total_basket_price/family_member

print("price of basket per person of week is ₹",basket_cost_per_person)

# part 2 - can items be shared eqally ?

print("\n\n\n")
total_item=int(input("Enter number of items : "))
people=int(input("Enter number of people : "))

if people==0:
    print("we cannot share items into 0 people")
elif total_item%people==0:
    print("each get equal items")
    print("each person get ",total_item//people," items")
else:
    print("items cannot be shared equally.\nitem left are ",total_item%people)

#part 3 - fix the weekly everage

recorded_average = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80

recorded_total = recorded_average * total_weeks              # 65 x 4  = 260
corrected_total = recorded_total - wrong_week_cost + correct_week_cost   # 260 - 50 + 80 = 290
corrected_average = corrected_total / total_weeks            # 290 / 4 = 72.5

print("Recorded total was:", recorded_total)
print("Corrected total is:", corrected_total)
print("Corrected weekly average:", corrected_average)


#part4 - compare with three stores

store_a_average = 70
store_b_average = 75
store_c_average = 80

print("Store A:", store_a_average, "| Store B:", store_b_average, "| Store C:", store_c_average)

if corrected_average < store_a_average and corrected_average < store_b_average and corrected_average < store_c_average:
    verdict = "cheaper than all three stores"
elif corrected_average > store_a_average and corrected_average > store_b_average and corrected_average > store_c_average:
    verdict = "more expensive than all three stores"
else:
    verdict = "somewhere in between the three stores"

print("Your average is", verdict)
4
# part 5 - the summary
print("\n=== SUMMARY ===")
print("Cost per person this week:", basket_cost_per_person)
print("Corrected weekly average :", corrected_average)
print("Verdict                  :", verdict)
