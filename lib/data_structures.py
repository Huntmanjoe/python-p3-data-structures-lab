spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    list_of_strings = []
    for food in spicy_foods:
        list_of_strings.append(food["name"])
    return list_of_strings

def get_spiciest_foods(spicy_foods):
    list_of_spiciest = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            list_of_spiciest.append(food)
    return list_of_spiciest
        

def print_spicy_foods(spicy_foods):
    chili_emoji = "🌶"
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {chili_emoji * food["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods: 
        if cuisine == food["cuisine"]:
            return food

def print_spiciest_foods(spicy_foods):
    chili_emoji = "🌶"
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {chili_emoji * food["heat_level"]}')

def get_average_heat_level(spicy_foods):
    total_number = 0
    for food in spicy_foods:
        total_number += food["heat_level"]
    new_average = total_number / len(spicy_foods)
    return new_average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
