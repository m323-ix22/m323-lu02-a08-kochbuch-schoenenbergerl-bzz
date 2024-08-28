"""
Dieses Modul enthält Funktionen zur Anpassung von Rezepten und zum Laden von Rezepten aus JSON.
"""

import json

def adjust_recipe(recipe, num_people):
    """Passt die Mengen der Zutaten an die Anzahl der Personen an."""
    adjusted_ingredients = {}
    original_servings = recipe['servings']
    factor = num_people / original_servings
    for ingredient, amount in recipe['ingredients'].items():
        adjusted_ingredients[ingredient] = amount * factor
    new_adjusted_recipe = {
        'title': recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people
    }
    return new_adjusted_recipe

def load_recipe(json_string):
    """Lädt ein Rezept aus einem JSON-String."""
    return json.loads(json_string)

if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = (
        '{"title": "Spaghetti Bolognese", "ingredients": '
        '{"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'
    )
    original_recipe = load_recipe(recipe_json)
    adjusted_recipe = adjust_recipe(original_recipe, 20)
    print(original_recipe)
    print(adjusted_recipe)
