import pytest 
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

def test_Ingredient_init():
    ingredient = Ingredient("Йогурт", 100.0, "г")

    assert ingredient.name == "Йогурт"
    assert ingredient.quantity == 100.0
    assert ingredient.unit == "г"

def test_Ingredient_float_quantity():
    ingredient1 = Ingredient("Йогурт", 100.0, "г")
    ingredient1.quantity = "150.0"
    ingredient2 = Ingredient("Молоко", "200.0", "мл")

    assert ingredient1.quantity == 150.0
    assert ingredient2.quantity == 200.0

def test_Ingredient_int_quantity():
    ingredient1 = Ingredient("Йогурт", 100.0, "г")
    ingredient1.quantity = 150
    ingredient2 = Ingredient("Молоко", 200, "мл")

    assert ingredient1.quantity == 150.0
    assert ingredient2.quantity == 200.0

def test_Ingredient_zero_quantity():
    with pytest.raises(ValueError):
        Ingredient("Йогурт", 0, "г")

def test_Ingredient_negative_quantity():
    with pytest.raises(ValueError):
        Ingredient("Йогурт", -50, "г")
    
def test_Ingredient_str():
    ingredient = Ingredient("Йогурт", 100.0, "г")

    assert str(ingredient) == "Йогурт: 100.0 г"

def test_Ingredient_repr():
    ingredient = Ingredient("Йогурт", 100.0, "г")

    assert repr(ingredient) == "Ingredient('Йогурт', 100.0, 'г')"

def test_Ingredient_eq_different_quantity():
    ingredient1 = Ingredient("Йогурт", 100.0, "г")
    ingredient2 = Ingredient("Йогурт", 10, "г")

    assert ingredient1 == ingredient2

def test_Ingredient_eq_different_name():
    ingredient1 = Ingredient("Йогурт", 100, "г")
    ingredient2 = Ingredient("Молоко", 100, "г")

    assert ingredient1 != ingredient2

def test_Ingredient_eq_different_unit():
    ingredient1 = Ingredient("Йогурт", 100, "г")
    ingredient2 = Ingredient("Йогурт", 100, "мл")

    assert ingredient1 != ingredient2

def test_Recipe_init():
    recipe = Recipe("Блины", [Ingredient("Йогурт", 100, "г."), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")])
    
    assert recipe.title == "Блины"
    assert recipe.ingredients == [Ingredient("Йогурт", 100, "г."), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")]

def test_Recipe_add_ingredient_new():
    recipe = Recipe("Блины", [Ingredient("Йогурт", 100, "г."), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")])
    recipe.add_ingredient(Ingredient("Сахар", 1, "ст.ложка"))

    assert recipe.ingredients == [Ingredient("Йогурт", 100, "г."), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт"), Ingredient("Сахар", 1, "ст.ложка")]

def test_Recipe_add_ingredient_same():
    recipe = Recipe("Блины", [Ingredient("Йогурт", 100, "г"), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")])
    recipe.add_ingredient(Ingredient("Йогурт", 50, "г"))

    assert recipe.ingredients == [Ingredient("Йогурт", 150, "г"), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")]

def test_Recipe_scale():
    recipe = Recipe("Блины", [Ingredient("Йогурт", 100, "г."), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")])
    new_recipe = recipe.scale(4)

    assert new_recipe.title  == "Блины"
    assert new_recipe.ingredients == [Ingredient("Йогурт", 400, "г."), Ingredient("Мука", 120, "г"), Ingredient("Яйца", 4, "шт")]
    assert new_recipe is not recipe

def test_Recipe_zero():
    recipe = Recipe("Блины", [Ingredient("Йогурт", 100, "г."), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")])
    
    with pytest.raises(ValueError):
        recipe.scale(0)

def test_Recipe_negative():
    recipe = Recipe("Блины", [Ingredient("Йогурт", 100, "г."), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")])
    
    with pytest.raises(ValueError):
        recipe.scale(-2)

def test_Recipe_len():
    recipe = Recipe("Блины", [Ingredient("Йогурт", 100, "г."), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")])
    
    assert len(recipe) == len(recipe.ingredients)

def test_ShoppingList_add_recipe_correct():
    shopping_list = ShoppingList()
    recipe = Recipe("Блины", [Ingredient("Йогурт", 100, "г."), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")]) 
    shopping_list.add_recipe(recipe, 2.0)

    assert shopping_list._items == [(Ingredient("Йогурт", 200, "г."), "Блины"), (Ingredient("Мука", 60, "г"), "Блины"), (Ingredient("Яйца", 2, "шт"), "Блины")]

def test_ShoppingList_add_recipe_incorrect():
    shopping_list = ShoppingList()
    recipe = Recipe("Блины", [Ingredient("Йогурт", 100, "г."), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")]) 
    with pytest.raises(ValueError):
        shopping_list.add_recipe(recipe, -1)

def test_ShoppingList_remove_recipe_have():
    shopping_list = ShoppingList()
    recipe1 = Recipe("Блины", [Ingredient("Йогурт", 100, "г."), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")]) 
    recipe2 = Recipe("Салат", [Ingredient("Огурцы", 1, "шт"), Ingredient("Помидоры", 1.5, "шт")])
    shopping_list.add_recipe(recipe1, 2.0)
    shopping_list.add_recipe(recipe2, 1)
    shopping_list.remove_recipe("Салат")

    assert shopping_list._items == [(Ingredient("Йогурт", 200, "г."), "Блины"), (Ingredient("Мука", 60, "г"), "Блины"), (Ingredient("Яйца", 2, "шт"), "Блины")]

def test_ShoppingList_get_list():
    shopping_list = ShoppingList()
    recipe1 = Recipe("Блины", [Ingredient("Йогурт", 100, "г."), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")]) 
    recipe2 = Recipe("Омлет", [Ingredient("Помидоры", 1.5, "шт"), Ingredient("Яйца", 2, "шт")])
    shopping_list.add_recipe(recipe1, 2.0)
    shopping_list.add_recipe(recipe2, 1)

    assert shopping_list.get_list() == [Ingredient("Йогурт", 200, "г."), Ingredient("Мука", 60, "г"), Ingredient("Помидоры", 1.5, "шт"), Ingredient("Яйца", 4, "шт")]

def test_ShoppingList_add():
    shopping_list1 = ShoppingList()
    shopping_list2 = ShoppingList()
    recipe1 = Recipe("Блины", [Ingredient("Йогурт", 100, "г."), Ingredient("Мука", 30, "г"), Ingredient("Яйца", 1, "шт")]) 
    recipe2 = Recipe("Омлет", [Ingredient("Помидоры", 1.5, "шт"), Ingredient("Яйца", 2, "шт")])
    shopping_list1.add_recipe(recipe1, 1)
    shopping_list2.add_recipe(recipe2, 1)
    new_list = shopping_list1 + shopping_list2

    assert new_list._items == [(Ingredient("Йогурт", 100, "г."), "Блины"), (Ingredient("Мука", 30, "г"), "Блины"), (Ingredient("Яйца", 1, "шт"), "Блины"), (Ingredient("Помидоры", 1.5, "шт"), "Омлет"), (Ingredient("Яйца", 2, "шт"), "Омлет")]
    assert shopping_list1._items == [(Ingredient("Йогурт", 100, "г."), "Блины"), (Ingredient("Мука", 30, "г"), "Блины"), (Ingredient("Яйца", 1, "шт"), "Блины")]
    assert shopping_list2._items ==  [(Ingredient("Помидоры", 1.5, "шт"), "Омлет"), (Ingredient("Яйца", 2, "шт"), "Омлет")]
   



