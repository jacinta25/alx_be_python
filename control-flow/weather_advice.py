weather = ("sunny", "rainy", "cold")
user_input = input(f"what's the weather like Today?{weather}: ")
if user_input == "sunny":
 print("wear a t-shirt and sunglasses")
elif user_input == "rainy":
 print("Don't forget your umbrella and a raincoat")
elif user_input == "cold":
 print("Make sure to wear a warm coat and a scarf")
else:
 print("Sorry, i don't have recommendations for this waether.")