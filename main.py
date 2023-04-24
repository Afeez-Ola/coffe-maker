from menu import MENU, resources

total_water = resources["water"]
total_milk = resources["milk"]
total_coffee = resources["coffee"]
process_coffee = True


def report_printing():
    for item, value in resources.items():
        result = f"{item}:{value}"
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
            if coffee_selected["ingredients"]["water"] <= resources["water"] and coffee_selected["ingredients"][
                "milk"] <= resources["milk"] and coffee_selected["ingredients"]["coffee"] <= \
                    resources["coffee"]:
                if user_payment >= coffee_cost:
                    resources["water"] = resources["water"] - coffee_selected["ingredients"]["water"]
                    resources["milk"] = resources["milk"] - coffee_selected["ingredients"]["milk"]
                    resources["coffee"] = resources["coffee"] - coffee_selected["ingredients"]["coffee"]
                    balance = round((user_payment - coffee_cost), 2)
                    resources["money"] += coffee_cost
                    print(f"Coffee Processed. {prompt} cost:${coffee_cost}. User payed: ${user_payment}")

                    if user_payment > coffee_cost:
                        print(f"Here is ${balance} dollars in change.")

                elif user_payment < coffee_cost:
                    print("“Sorry that's not enough money. Money refunded.")
            else:
                print("Coffee can not processed because of insufficient resources.")
            still_buying = input("Do you want to make another purchase? Type 'yes' or 'no': ")
            if still_buying == 'yes':
                process_coffee = True
            elif still_buying == "report":
                (report_printing())
                still_buying = input("Do you want to make a purchase? Type 'yes' or 'no': ")
                if still_buying == 'yes':
                    process_coffee = True
                else:
                    process_coffee = False

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
