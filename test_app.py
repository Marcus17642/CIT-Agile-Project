import pytest


from db import db
from models import User, Food, Meal, FoodMeal
import app, manage


def test_validate_user_data_nominal():
    """
    GIVEN a user class to validate the form data
    WHEN valid data is passed in
    THEN check that the validation is successful
    """
    user_data = User(
        name='tom',
        phone=123456789,
        height= 100,
        weight=70,
        gender= "male",
        age= 25,
        tdee= 200,
        password= "abcd1234"
    
    )
    assert user_data.name == 'tom'
    assert user_data.phone == 123456789
    assert user_data.height == 100
    assert user_data.weight == 70
    assert user_data.gender == "male"
    assert user_data.age == 25
    assert user_data.tdee == 200

# def test_validate_user_data_missing_name():
#     """
#     GIVEN a user class to validate the form data
#     WHEN the name field is missing
#     THEN check that the validation fails
#     """
#     with pytest.raises(TypeError):
#         user_data = User(
#             phone=123456789,
#             height= 100,
#             weight=70)


def test_validate_food_data_nominal():
    """
    GIVEN a food class to validate
    WHEN valid data is passed in
    THEN check that the validation is successful
    """
    food_data = Food(
        name='apple',
        calories= 100,
        protein= 10,
        carbs= 20,
        fat= 5
    )
    assert food_data.name == 'apple'
    assert food_data.calories == 100
    assert food_data.protein == 10
    assert food_data.carbs == 20
    assert food_data.fat == 5
            
def test_validate_meal_data_nominal():
    """
    GIVEN a meal class to validate
    WHEN valid data is passed in
    THEN check that the validation is successful
    """
    meal_data = Meal(
        name='breakfast',
        user_id= 1,

    )
    assert meal_data.name == 'breakfast'
    assert meal_data.user_id == 1

def test_validate_foodmeal_data_nominal():
    """
    GIVEN a foodmeal class to validate
    WHEN valid data is passed in
    THEN check that the validation is successful
    """
    foodmeal_data = FoodMeal(
        meal_id= 1,
        food_id= 1,
        amount= 100
    )
    assert foodmeal_data.meal_id == 1
    assert foodmeal_data.food_id == 1
    assert foodmeal_data.amount == 100

