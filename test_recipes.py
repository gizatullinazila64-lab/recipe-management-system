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

def test_Ingredient_invalid_quantity():
    with pytest.raises(ValueError):
        Ingredient("Йогурт", "шт", "г")
    
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

def test_Ingredient_eq_different_name_unit():
    ingredient1 = Ingredient("Йогурт", 100, "г")
    ingredient2 = Ingredient("Молоко", 100, "г")
    ingredient3 = Ingredient("Йогурт", 100, "мл")

    assert ingredient1 != ingredient2
    assert ingredient1 != ingredient3

def test_Ingredient_eq_different_type():
    ingredient1 = Ingredient("Йогурт", 100, "г")
    ingredient2 = "Йогурт 100 г"

    assert ingredient1 != ingredient2


    