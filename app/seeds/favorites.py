from app.models import db, Favorite, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_favorites():
    favorite1 = Favorite(
        user_id=1,
        product_id=1,
        favorited_at=datetime.now()
    )
    favorite2 = Favorite(
        user_id=2,
        product_id=2,
        favorited_at=datetime.now()
    )
    favorite3 = Favorite(
        user_id=3,
        product_id=3,
        favorited_at=datetime.now()
    )

    db.session.add_all([favorite1, favorite2, favorite3])
    db.session.commit()

def undo_favorites():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.favorites RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM favorites"))
    db.session.commit()
