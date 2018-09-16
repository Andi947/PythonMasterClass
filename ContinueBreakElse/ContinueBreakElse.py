# shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shoppingList:
#     if item == "spam":
#         print("I'm ignoring " + item)
#         # continue  - skips this item
#         break  # ends the loop
#     print("Buy " + item)

meal = ["egg", "bacon", "tomato", "sausages"]   # if thousands of items - don't need to process further using break
nastyFoodItem = ''   # definition preferred here
for item in meal:
    if item == "spam":
        nastyFoodItem = item   # Python has various convention - nasty_food_item / nastyFoodItem
        break
else:
    print("I'll have a plate of that please")

if nastyFoodItem:
    print("Can't I have anything without spam in it!?")
