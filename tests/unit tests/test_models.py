import sys
import pytest
sys.path.append('C:\\Users\\user\\Documents\\CIT term 2\\Agile project\\second repository\\CIT-Agile-Project') 
# we will have tests that test each function individually

# go over this quickly. Here we're testing this. Here we're testing that etc 
from models import Food, User, Meal, FoodMeal
import app, manage

@pytest.fixture
def sample_food():
    return Food(id=1, name="Test Food", calories=100, protein=10, fat=5, carbs=20)

@pytest.fixture
def sample_user():
    return User(id=1, name="Test User", phone="123456789", height=170.0, weight=70.0, gender="Male", age=25, password="testpassword")

def test_toDict(sample_food):
    """
    GIVEN a food class to validate
    WHEN valid data is passed in
    THEN check that the validation is successful
    """

    food_dict = sample_food.toDict()

    assert food_dict == {"id": 1, "name": "Test Food", "calories": 100, "protein": 10, "fat": 5, "carbs": 20}



def test_user(sample_user):
    """
    GIVEN a user class to validate the form data
    WHEN valid data is passed in
    THEN check that the validation is successful
    """
    assert sample_user.name == "Test User"
    assert sample_user.phone == "123456789"
    assert sample_user.height == 170.0
    assert sample_user.weight == 70.0
    assert sample_user.gender == "Male"
    assert sample_user.age == 25
    assert sample_user.password == "testpassword"


def test_getTotalMacros_with_no_meals(sample_user):
    # When the user has no meals, the total macros should be zero
    total_macros = sample_user.getTotalMacros()
    assert total_macros == {"fat": 0, "protein": 0, "carbs": 0, "calories": 0}


            
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
