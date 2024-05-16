from flask import url_for
import sys
import pytest
sys.path.append('C:\\Users\\user\\Documents\\CIT term 2\\Agile project\\second repository\\CIT-Agile-Project') # Adjust the path accordingly
from app import app, db

from models import Food, Meal, FoodMeal
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Home' in response.data

def test_food(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data

#this is a wrong unit test for posting
"""
def test_post(client):
    response = client.post('/', data={'key': 'value'})
    assert response.status_code == 200
    assert b'Home' in response.data


def test_add_foodmeal(client):
    # Create a test meal and food
    meal = Meal(id=1)
    food = Food(id=1)
    db.session.add(meal)
    db.session.add(food)
    db.session.commit()

    # Send a POST request with valid data
    data = {"food_id": [1, 2], "amount": [10, 20]}
    response = client.post('/users/1/addfoodmeal/1', data=data, content_type='application/x-www-form-urlencoded')

    # Assert response status code and content
    assert response.status_code == 201
    assert response.json() == {"message": "Food meals added successfully"}

    # Assert food meals were created in the database
    food_meals = FoodMeal.query.all()
    assert len(food_meals) == 2
    assert food_meals[0].meal_id == 1
    assert food_meals[0].food_id == 1
    assert food_meals[0].amount == 10
    assert food_meals[1].meal_id == 1
    assert food_meals[1].food_id == 2
    assert food_meals[1].amount == 20

    # Test invalid input data
    data = {"food_id": [1, 2], "amount": [10]}  # mismatched lengths
    response = client.post('/users/1/addfoodmeal/1', data=data, content_type='application/x-www-form-urlencoded')
    assert response.status_code == 400
    assert response.json() == {"error": "Invalid input data"}


def test_add_foodmeal(client):
    # Assuming you have test users and meals created in your database
    user_id = 1
    meal_id = 1
    data = {
        "food_id": [1, 2],  # Assuming you have food IDs in your database
        "amount": [100, 200]  # Amounts corresponding to each food
    }
    response = client.post(url_for('add_foodmeal', user_id=user_id, meal_id=meal_id), data=data)
    
    # Check if the response status code is 302 (redirect)
    assert response.status_code == 302
    
    # Optionally, you can check if the FoodMeal objects are added to the database correctly
    food_meals = FoodMeal.query.filter_by(meal_id=meal_id).all()
    assert len(food_meals) == 2  # Assuming two food items were 
    
"""