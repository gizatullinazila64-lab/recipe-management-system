class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str) -> None:
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self) -> float:
        return self._quantity

    @quantity.setter
    def quantity(self, value) -> None:
        value = float(value)
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = value

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self) -> str:
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    
    def __eq__(self, other: "Ingredient") -> bool:
        if not isinstance(other, Ingredient):
            return False
        return (self.name == other.name and self.unit == other.unit)


class Recipe:
    def __init__(self, title: str, ingredients: list[Ingredient]) -> None:
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient: Ingredient) -> None:
        flag = False
        for ing in self.ingredients:
            if ing == ingredient:
                ing.quantity += ingredient.quantity
                flag = True
                break
        if not flag:
            self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        if isinstance(ratio, (int, float)) and ratio > 0:
            return True
        return False

    def scale (self, ratio: float) -> "Recipe":
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Коэффициент масштабирования должен быть положительным числом")

        new_recipe = Recipe(self.title, [])
        for ingredient in self.ingredients:
            new_recipe.add_ingredient(Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit))
        return new_recipe

    def __len__(self) -> int:
        return len(self.ingredients)

    def __str__(self) -> str:
       return f"{self.title}:\n" + "\n".join(str(ing) for ing in self.ingredients) 


class ShoppingList:
    def __init__(self) -> None:
        self._items = []

    def add_recipe(self, recipe: Recipe, portion: float) -> None:
        if portion <= 0:
            raise ValueError("Количество порций должно быть положительным")
        
        new_recipe = recipe.scale(portion)
        for ingredient in new_recipe.ingredients:
            self._items.append((ingredient, recipe.title))
    
    def remove_recipe(self, title: str) -> None:
        copy = self._items.copy()
        for item in self._items:
            if item[1] == title:
                copy.remove(item)
        self._items = copy
    
    def get_list(self) -> list[Ingredient]:
        result = {}
        for item in self._items:
            ingredient = item[0]
            if (ingredient.name, ingredient.unit) in result:
                result[(ingredient.name, ingredient.unit)] += ingredient.quantity
            else:
                result[(ingredient.name, ingredient.unit)] = ingredient.quantity

        final_list = []
        for item in result.items():
            name, unit = item[0]
            quantity = item[1]
            final_list.append(Ingredient(name, quantity, unit))
        
        return sorted(final_list, key = lambda ingredient: ingredient.name)
    
    def __add__(self, other: "ShoppingList") -> "ShoppingList":
        new_list = ShoppingList()
        for item in self._items:
            new_list._items.append(item)
        for item in other._items:
            new_list._items.append(item)

        return new_list