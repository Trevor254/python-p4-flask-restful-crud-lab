#!/usr/bin/env python3

from app import app
from models import db, Plant

with app.app_context():
    print("🔄 Seeding database...")  # Debugging line

    # Delete existing plants
    try:
        Plant.query.delete()
        db.session.commit()
        print("🗑️ Existing plant records deleted.")  # Debugging line
    except Exception as e:
        print(f"❌ Error deleting plants: {e}")  # Error handling

    # Create new plant records
    try:
        aloe = Plant(
            id=1,
            name="Aloe",
            image="./images/aloe.jpg",
            price=11.50,
            is_in_stock=True,
        )

        zz_plant = Plant(
            id=2,
            name="ZZ Plant",
            image="./images/zz-plant.jpg",
            price=25.98,
            is_in_stock=False,
        )

        db.session.add_all([aloe, zz_plant])
        db.session.commit()
        print("✅ Seeding complete! Plants added.")  # Debugging line
    except Exception as e:
        print(f"❌ Error inserting plants: {e}")  # Error handling