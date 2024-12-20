from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class ProductImage(db.Model):
    __tablename__ = 'product_images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')), nullable=False)
    preview_image = db.Column(db.Boolean, default=False)
    image_url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    product = db.relationship("Product", back_populates="product_images")

    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'preview_image': self.preview_image,
            'image_url': self.image_url,
            'created_at': self.created_at
        }
