from menu import MENU, resources

total_water = resources["water"]
total_milk = resources["milk"]
total_coffee = resources["coffee"]
process_coffee = True


def report_printing():
    for item, value in resources.items():
        result = (f"{item}:{value}")
        print(result)

def payment_process():
    quarter_prompt = int(input("\nHow many quarter are you paying?: "))
    dime_prompt = int(input("How many dime are you paying?: "))
    nickel_prompt = int(input("How many nickel are you paying?: "))
    penny_prompt = int(input("How many penny are you paying?: "))

    total_quarters = quarter_prompt * 0.25
    total_dimes = dime_prompt * 0.10
    total_nickels = nickel_prompt * 0.05
    total_pennies = penny_prompt * 0.01

    user_payment = round((total_quarters + total_pennies + total_nickels + total_dimes), 2)
    return user_payment
def coffee_selection():
    global process_coffee
    while process_coffee:
        prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()


        if prompt in ["espresso", "latte", "cappuccino"]:
            user_payment = payment_process()
            coffee_selected = MENU[prompt]
            coffee_cost = coffee_selected["cost"]
            # checking if there's enough resources to make cappuccino
            if coffee_selected["ingredients"]["water"] <= resources["water"] and coffee_selected["ingredients"]["milk"] <= resources["milk"] and coffee_selected["ingredients"]["coffee"] <= \
                    resources["coffee"]:
                if user_payment >= coffee_cost:
                    resources["water"] = resources["water"] - coffee_selected["ingredients"]["water"]
                    resources["milk"] = resources["milk"] - coffee_selected["ingredients"]["milk"]
                    resources["coffee"] = resources["coffee"] - coffee_selected["ingredients"]["coffee"]
                    balance = round((user_payment - coffee_cost), 2)
                    resources["money"] += coffee_cost
                    print(f"Coffee Processed. {prompt} cost:${coffee_cost}. User payed: {user_payment}")

                    if user_payment > coffee_cost:
                        print(f"Here is ${balance} dollars in change.")

                elif user_payment < coffee_cost:
                    print("“Sorry that's not enough money. Money refunded.")
            else:
                print("Coffee can not processed because of insufficient resources.")
            still_buying = input("Do you want to make another purchase? Type 'yes' or 'no': ")
            if still_buying == 'yes':
                process_coffee = True
            else:
                process_coffee = False

        elif prompt == 'report':
            (report_printing())
            still_buying = input("Do you want to make a purchase? Type 'yes' or 'no': ")
            if still_buying == 'yes':
                process_coffee = True
            else:
                process_coffee = False

coffee_selection()


#Here is the refactored code.

# def report_printing():
#     for item, value in resources.items():
#         print(f"{item}: {value}")
#
# def process_payment(selected_coffee):
#     quarters_unit = 0.25
#     dimes_unit = 0.10
#     nickels_unit = 0.05
#     pennies_unit = 0.01
#
#     quarter_prompt = int(input("\nHow many quarters are you paying?: "))
#     dime_prompt = int(input("How many dimes are you paying?: "))
#     nickel_prompt = int(input("How many nickels are you paying?: "))
#     penny_prompt = int(input("How many pennies are you paying?: "))
#
#     total_quarters = quarter_prompt * quarters_unit
#     total_dimes = dime_prompt * dimes_unit
#     total_nickels = nickel_prompt * nickels_unit
#     total_pennies = penny_prompt * pennies_unit
#
#     user_payment = round((total_quarters + total_pennies + total_nickels + total_dimes), 2)
#     coffee_cost = selected_coffee["cost"]
#
#     if user_payment >= coffee_cost:
#         change = round(user_payment - coffee_cost, 2)
#         resources["money"] += coffee_cost
#         print(f"Here is ${change} in change.")
#         return True
#     else:
#         print("Sorry, that's not enough money. Money refunded.")
#         return False
#
# def process_coffee():
#     while True:
#         prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
#         if prompt == 'report':
#             report_printing()
#         elif prompt in ['espresso', 'latte', 'cappuccino']:
#             selected_coffee = MENU[prompt]
#             if selected_coffee["ingredients"]["water"] <= resources["water"] and selected_coffee["ingredients"]["milk"] <= resources["milk"] and selected_coffee["ingredients"]["coffee"] <= resources["coffee"]:
#                 if process_payment(selected_coffee):
#                     resources["water"] -= selected_coffee["ingredients"]["water"]
#                     resources["milk"] -= selected_coffee["ingredients"]["milk"]
#                     resources["coffee"] -= selected_coffee["ingredients"]["coffee"]
#                     print(f"Here is your {prompt}. Enjoy!")
#             else:
#                 print("Sorry, there are not enough resources to make your selection.")
#         else:
#             print("Invalid selection. Please try again.")
#
#         still_buying = input("Would you like to order another coffee? (y/n): ").lower()
#         if still_buying != 'y':
#             break
#
# process_coffee()
