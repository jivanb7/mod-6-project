from app.models import db, Product
from datetime import datetime

def seed_products():
    product1 = Product(
        user_id=1,
        category="Electronics",
        name="Smartphone",
        description="A powerful smartphone with a sleek design",
        price=699.99,
        stock=50,
        created_at=datetime.now()
    )
    product2 = Product(
        user_id=2,
        category="Home Appliance",
        name="Blender",
        description="High-speed blender for smoothies and sauces",
        price=89.99,
        stock=120,
        created_at=datetime.now()
    )
    product3 = Product(
        user_id=3,
        category="Fashion",
        name="Designer Jacket",
        description="Stylish and warm designer jacket",
        price=249.99,
        stock=30,
        created_at=datetime.now()
    )

    db.session.add_all([product1, product2, product3])
    db.session.commit()


def undo_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))
    db.session.commit()
