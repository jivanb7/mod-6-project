from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from app.models import User, db, Favorite, Product, ProductImage

favorite_routes = Blueprint('favorites', __name__)

@favorite_routes.route('/current', methods=['GET'])
@login_required
def get_favorites():
    """
    Get all the favorite products for the logged-in user, including preview image.
    """
    favorites = Favorite.query.filter_by(user_id=current_user.id).all()

    favorite_products = []
    for favorite in favorites:
        product = Product.query.get(favorite.product_id)
        if product:
            # Retrieve the preview image for the product
            preview_image = ProductImage.query.filter_by(product_id=product.id, preview_image=True).first()
            product_data = product.to_dict()
            if preview_image:
                product_data['preview_image'] = preview_image.image_url  # Add preview image URL
            favorite_products.append(product_data)

    return jsonify(favorite_products), 200


@favorite_routes.route('/<int:product_id>', methods=['POST'])
@login_required
def add_favorite(product_id):
    """
    Add a product to the logged-in user's favorites.
    """

    # Check if the product is already in the user's favorites
    existing_favorite = Favorite.query.filter_by(user_id=current_user.id, product_id=product_id).first()

    if existing_favorite:
        return jsonify({'message': 'Product is already in favorites'}), 409

    new_favorite = Favorite(user_id=current_user.id, product_id=product_id)
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify({'message': 'Product added to favorites'}), 201


@favorite_routes.route('/<int:product_id>', methods=['DELETE'])
@login_required
def remove_favorite(product_id):
    """
    Remove a product from the logged-in user's favorites.
    """
    favorite = Favorite.query.filter_by(user_id=current_user.id, product_id=product_id).first()

    if not favorite:
        return jsonify({'error': 'Favorite not found'}), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify({'message': 'Product removed from favorites'}), 200