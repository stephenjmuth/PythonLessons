

 available_toppings = ['mushrooms', 'olives', 'green peppers',
                         'pepperoni', 'pineapple', 'extra cheese']
➋ requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

➌ for requested_topping in requested_toppings:
➍     if requested_topping in available_toppings:
           print(f"Adding {requested_topping}.")
➎     else:
           print(f"Sorry, we don't have {requested_topping}.")

   print("\nFinished making your pizza!")