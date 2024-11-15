from app.models import db, Order, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_orders():
    order1 = Order(
        user_id=1,
        details='Decorative Stone, 5, $29.99; Waterfall Fountain, 1, $79.99',
        total=109.98,
        created_at=datetime.now()
    )
    order2 = Order(
        user_id=2,
        details='Acer-5 Laptop, 1, $899.99; Acer-3 Desktop, 1, $599.99',
        total=1499.98,
        created_at=datetime.now()
    )
    order3 = Order(
        user_id=3, 
        details='Christmas Tree, 1, $49.99',
        total=49.99,
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
