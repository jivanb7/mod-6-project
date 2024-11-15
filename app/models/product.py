from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    category = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    user = db.relationship("User", back_populates="products")
    reviews = db.relationship("Review", back_populates="product", cascade='all, delete')
    shopping_carts = db.relationship("ShoppingCart", back_populates="product", cascade='all, delete')
    favorites = db.relationship("Favorite", back_populates="product", cascade='all, delete')
    product_images = db.relationship("ProductImage", back_populates="product", cascade='all, delete')

    def calculate_average_rating(self):
        if not self.reviews:
            return None
        total_rating = sum(review.rating for review in self.reviews)
        return round(total_rating / len(self.reviews), 1)

    def to_dict(self):
        preview_image_url = None
        for image in self.product_images:
            if image.preview_image:
                preview_image_url = image.image_url
                break

        return {
            'id': self.id,
            'user_id': self.user_id,
            'username': self.user.username, 
            'category': self.category,
            'name': self.name,
            'description': self.description,
            'price': float(self.price),
            'stock': self.stock,
            'created_at': self.created_at,
            'previewImage': preview_image_url, 
            'average_rating': self.calculate_average_rating(),
            'review_count': len(self.reviews)
        }
