from app.models import db, ProductImage, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_product_images():
    image1 = ProductImage(
        product_id=1,
        preview_image=True,
        image_url="https://example.com/image1.jpg",
        created_at=datetime.now()
    )
    image2 = ProductImage(
        product_id=2,
        preview_image=False,
        image_url="https://example.com/image2.jpg",
        created_at=datetime.now()
    )
    image3 = ProductImage(
        product_id=3,
        preview_image=True,
        image_url="https://example.com/image3.jpg",
        created_at=datetime.now()
    )

    db.session.add_all([image1, image2, image3])
    db.session.commit()

def undo_product_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.product_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM product_images"))
    db.session.commit()
