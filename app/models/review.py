from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')))
    comment = db.Column(db.Text)
    item_quality = db.Column(db.Integer)
    shipping = db.Column(db.Integer)
    customer_service = db.Column(db.Integer)
    recommended = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    user = db.relationship("User", back_populates="reviews")
    product = db.relationship("Product", back_populates="reviews")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'product_id': self.product_id,
            'comment': self.comment,
            'item_quality': self.item_quality,
            'shipping': self.shipping,
            'customer_service': self.customer_service,
            'recommended': self.recommended,
            'created_at': self.created_at
        }
