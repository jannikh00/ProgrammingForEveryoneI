
# declaring recipe name, ingredients list and list including the steps to prepare recipe 1, which is "Spaghetti Bolognese"
recipe_1_name = "Spaghetti Bolognese"
recipe_1_ingredients = ["Spaghetti", "Ground Beef", "Tomato Sauce", "Onion", "Garlic", "Olive Oil", "Salt", "Pepper"]
recipe_1_steps = [
    "Boil the spaghetti according to the instructions on the package.",
    "While the spaghetti is boiling, chop the onion and garlic.",
    "Heat some olive oil in a pan.",
    "Add the onion and garlic to the pan and sauté until the onion is translucent.",
    "Add the ground beef to the pan and cook until browned.",
    "Add the tomato sauce to the pan, and season with salt and pepper.",
    "Simmer the sauce for 15 minutes.",
    "Serve the sauce over the cooked spaghetti."
]

# declaring recipe name, ingredients list and list including the steps to prepare recipe 2, which is "Chicken Tikka Masala"
recipe_2_name = "Chicken Tikka Masala"
recipe_2_ingredients = ["Chicken Breast", "Tikka Masala Sauce", "Rice", "Yogurt", "Cilantro", "Salt", "Pepper"]
recipe_2_steps = [
    "Cook the rice according to the instructions on the package.",
    "While the rice is cooking, cut the chicken breast into cubes.",
    "Heat some oil in a pan.",
    "Add the chicken to the pan and cook until browned.",
    "Add the tikka masala sauce to the pan, and season with salt and pepper.",
    "Simmer the sauce for 15 minutes.",
    "Serve the sauce over the cooked rice, with a dollop of yogurt and some cilantro on top."
]

# declaring recipe name, ingredients list and list including the steps to prepare recipe 3, which is "Chocolate Chip Cookies"
recipe_3_name = "Chocolate Chip Cookies"
recipe_3_ingredients = ["Flour", "Butter", "Sugar", "Brown Sugar", "Eggs", "Vanilla Extract", "Baking Soda", "Salt", "Chocolate Chips"]
recipe_3_steps = [
    "Preheat your oven to 375 degrees F (190 degrees C).",
    "In a large bowl, cream together the butter, sugar, and brown sugar.",
    "Beat in the eggs one at a time, then stir in the vanilla.",
    "In a separate bowl, combine the flour, baking soda, and salt; gradually add to the butter mixture until well combined.",
    "Fold in the chocolate chips.",
    "Drop by rounded spoonfuls onto ungreased cookie sheets.",
    "Bake for 9 to 11 minutes, or until golden brown."
]

# function to print the recipe name, ingredient list and the steps to prepare the recipe
def print_info(recipe, ingredients, steps):
    print(f"Recipe: {recipe}")
    print("Ingredients:")
    for ingredient in ingredients:
        print(f" - {ingredient}")
    print("Steps:")
    for i, step in enumerate(steps):
        print(f" {i+1}. {step}")
    print("\n")

# printing the 3 given recipes using the function
print_info(recipe_1_name, recipe_1_ingredients, recipe_1_steps)
print_info(recipe_2_name, recipe_2_ingredients, recipe_2_steps)
print_info(recipe_3_name, recipe_3_ingredients, recipe_3_steps)

