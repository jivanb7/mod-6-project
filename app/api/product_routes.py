from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Product, db, Review

product_routes = Blueprint('products', __name__)

@product_routes.route('/', methods=['GET'])
def get_all_products():
    """
    Get all the products from the database.
    """
    products = Product.query.all()
    product_list = [product.to_dict() for product in products]

    return jsonify(product_list), 200

@product_routes.route('/current', methods=['GET'])
@login_required 
def get_user_products():
    """
    Get all the products of the current logged-in user.
    """
    products = Product.query.filter_by(user_id=current_user.id).all()
    product_list = [product.to_dict() for product in products]

    return jsonify(product_list), 200

@product_routes.route('/<int:product_id>', methods=['GET'])
def get_product_detail(product_id):
    """
    Get the details of a specific product by its ID.
    """
    product = Product.query.get(product_id)

    if not product:
        return jsonify({'error': 'Product not found'}), 404

    return jsonify(product.to_dict()), 200

@product_routes.route('/', methods=['POST'])
@login_required
def create_product():
    """
    Create a new product by the logged-in user.
    """
    data = request.get_json()

    category = data.get('category')
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    stock = data.get('stock')

    if category is None:
        return jsonify({'error': 'Category is required'}), 400
    if name is None:
        return jsonify({'error': 'Name is required'}), 400
    if description is None:
        return jsonify({'error': 'Description is required'}), 400
    if price is None:
        return jsonify({'error': 'Price is required'}), 400
    if stock is None:
        return jsonify({'error': 'Stock is required'}), 400

    new_product = Product(
        category=category,
        name=name,
        description=description,
        price=price,
        stock=stock,
        user_id=current_user.id 
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify(new_product.to_dict()), 201

@product_routes.route('/<int:product_id>', methods=['PUT'])
@login_required 
def update_product(product_id):
    """
    Update the details of an existing product by the logged-in user.
    Only the owner of the product can update it.
    """
    product = Product.query.get(product_id)

    if not product:
        return jsonify({'error': 'Product not found'}), 404

    if product.user_id != current_user.id:
        return jsonify({'error': 'You are not authorized to edit this product'}), 403

    data = request.get_json()

    category = data.get('category', product.category)
    name = data.get('name', product.name)
    description = data.get('description', product.description) 
    price = data.get('price', product.price)
    stock = data.get('stock', product.stock) 

    product.category = category
    product.name = name
    product.description = description
    product.price = price
    product.stock = stock

    db.session.commit()

    return jsonify(product.to_dict()), 200

@product_routes.route('/<int:product_id>', methods=['DELETE'])
@login_required 
def delete_product(product_id):
    """
    Delete a product by its ID, only if the logged-in user is the owner.
    """
    product = Product.query.get(product_id)

    if not product:
        return jsonify({'error': 'Product not found'}), 404

    if product.user_id != current_user.id:
        return jsonify({'error': 'You are not authorized to delete this product'}), 403

    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'Product deleted successfully'}), 200

@product_routes.route('/<int:product_id>/reviews', methods=['GET'])
def get_product_reviews(product_id):
    """
    Get all reviews for a specific product by its product ID.
    """
    reviews = Review.query.filter_by(product_id=product_id).all()

    if not reviews:
        return jsonify({'message': 'No reviews found for this product'}), 404

    return jsonify([review.to_dict() for review in reviews]), 200

@product_routes.route('/<int:product_id>/reviews', methods=['POST'])
@login_required 
def create_review(product_id):
    """
    Create a new review for a product.
    Only authenticated users can leave a review.
    The product owner cannot review their own product.
    """
    product = Product.query.get(product_id)

    if not product:
        return jsonify({'error': 'Product not found'}), 404

    if product.user_id == current_user.id:
        return jsonify({'error': 'You cannot review your own product'}), 400

    data = request.get_json()

    item_quality = data.get('item_quality')
    shipping = data.get('shipping')
    customer_service = data.get('customer_service')
    comment = data.get('comment')

    if None in [item_quality, shipping, customer_service, comment]:
        return jsonify({'error': 'Item quality, shipping, customer service, and comment are required'}), 400

    if not (1 <= item_quality <= 5) or not (1 <= shipping <= 5) or not (1 <= customer_service <= 5):
        return jsonify({'error': 'Ratings must be between 1 and 5'}), 400
    
    ##Rating calculation
    rating = round((item_quality + shipping + customer_service) / 3)

    new_review = Review(
        user_id=current_user.id,
        product_id=product.id,
        comment=comment,
        item_quality=item_quality,
        shipping=shipping,
        customer_service=customer_service,
        rating=rating,
        recommended=rating >= 4
    )

    db.session.add(new_review)
    db.session.commit()

    return jsonify(new_review.to_dict()), 201

