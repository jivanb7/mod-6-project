from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import ShoppingCart, Product, db

cart_routes = Blueprint('cart', __name__)

@cart_routes.route('/current', methods=['GET'])
@login_required  
def get_cart():
    """
    Get all products in the logged-in user's cart.
    """
    cart_items = ShoppingCart.query.filter_by(user_id=current_user.id).all()

    if not cart_items:
        return jsonify({'message': 'Your cart is empty'}), 200

    cart_products = []
    for item in cart_items:
        product = Product.query.get(item.product_id)
        if product:
            cart_products.append({
                'product_id': product.id,
                'name': product.name,
                'price': product.price,
                'quantity': item.quantity,
                'total_price': item.quantity * product.price
            })

    return jsonify(cart_products), 200

@cart_routes.route('/', methods=['POST'])
@login_required 
def add_to_cart():
    """
    Add a product to the logged-in user's shopping cart.
    """
    data = request.get_json()
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1) 

    if not product_id or quantity <= 0:
        return jsonify({'error': 'Invalid product ID or quantity'}), 400

    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    cart_item = ShoppingCart.query.filter_by(user_id=current_user.id, product_id=product_id).first()

    if cart_item:
        cart_item.quantity += quantity
        db.session.commit()
        return jsonify({'message': 'Product quantity updated in the cart'}), 200
    else:
        new_cart_item = ShoppingCart(
            user_id=current_user.id,
            product_id=product_id,
            quantity=quantity
        )
        db.session.add(new_cart_item)
        db.session.commit()
        return jsonify({'message': 'Product added to the cart'}), 201

@cart_routes.route('/<int:cart_item_id>', methods=['PUT'])
@login_required 
def edit_cart_quantity(cart_item_id):
    """
    Edit the quantity of a product in the logged-in user's cart.
    """
    data = request.get_json()
    quantity = data.get('quantity')

    if not quantity or quantity <= 0:
        return jsonify({'error': 'Invalid quantity'}), 400

    cart_item = ShoppingCart.query.filter_by(id=cart_item_id, user_id=current_user.id).first()

    if not cart_item:
        return jsonify({'error': 'Cart item not found'}), 404

    cart_item.quantity = quantity
    db.session.commit()

    return jsonify({'message': 'Cart quantity updated successfully', 'cart_item': cart_item.to_dict()}), 200

@cart_routes.route('/<int:cart_item_id>', methods=['DELETE'])
@login_required 
def delete_cart_item(cart_item_id):
    """
    Delete a product from the logged-in user's cart.
    """
    cart_item = ShoppingCart.query.filter_by(id=cart_item_id, user_id=current_user.id).first()

    if not cart_item:
        return jsonify({'error': 'Cart item not found'}), 404

    db.session.delete(cart_item)
    db.session.commit()

    return jsonify({'message': 'Product removed from cart successfully'}), 200