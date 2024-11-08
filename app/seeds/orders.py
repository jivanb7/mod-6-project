from app.models import db, Order, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_orders():
    order1 = Order(
        user_id=1, 
        product_id=1, 
        quantity=1, 
        total=699.99, 
        created_at=datetime.now()
    )
    order2 = Order(
        user_id=2, 
        product_id=2, 
        quantity=2, 
        total=179.98, 
        created_at=datetime.now()
    )
    order3 = Order(
        user_id=3, 
        product_id=3, 
        quantity=1, 
        total=19.99, 
        created_at=datetime.now()
    )

    db.session.add_all([order1, order2, order3])
    db.session.commit()

def undo_orders():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.orders RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM orders"))
    db.session.commit()
