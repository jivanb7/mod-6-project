from app.models import db, ShoppingCart, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_shopping_carts():
    cart1 = ShoppingCart(
        user_id=1,
        product_id=1,
        quantity=1,
        added_at=datetime.now()
    )
    cart2 = ShoppingCart(
        user_id=2,
        product_id=2,
        quantity=2,
        added_at=datetime.now()
    )
    cart3 = ShoppingCart(
        user_id=3,
        product_id=3,
        quantity=1,
        added_at=datetime.now()
    )

    db.session.add_all([cart1, cart2, cart3])
    db.session.commit()

def undo_shopping_carts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.shopping_carts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM shopping_carts"))
    db.session.commit()
