from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_reviews():
    review1 = Review(
        user_id=1,
        product_id=1,
        rating=5,
        comment="Absolutely love this phone!",
        item_quality=5,
        shipping=4,
        customer_service=5,
        recommended=True,
        created_at=datetime.now()
    )
    review2 = Review(
        user_id=2,
        product_id=2,
        rating=4,
        comment="Great blender, but a bit noisy.",
        item_quality=4,
        shipping=5,
        customer_service=4,
        recommended=True,
        created_at=datetime.now()
    )
    review3 = Review(
        user_id=3,
        product_id=3,
        rating=3,
        comment="Nice jacket, but not my style.",
        item_quality=4,
        shipping=3,
        customer_service=4,
        recommended=False,
        created_at=datetime.now()
    )

    db.session.add_all([review1, review2, review3])
    db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))
    db.session.commit()
