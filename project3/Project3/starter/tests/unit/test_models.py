import pytest
from app import create_app
from app.models import Fruit, FruitMetrics, db

def test_createFruit_withValidData_createsFruitWithCorrectAttributes():
    app = create_app()
    app.config["TESTING"] = True

    with app.app_context():
        fruit = Fruit(name="Apple", quantity=1, variety="Gala", season="Fall")
        db.session.add(fruit)
        db.session.commit()

        assert fruit.name == "Apple"
