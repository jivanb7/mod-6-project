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
                'id': item.id,
                'product_id': product.id,
                'name': product.name,
                'price': float(product.price),
                'quantity': item.quantity,
                'total_price': float(item.quantity * product.price)
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
    if product.stock < quantity:
        return jsonify({'error': 'Insufficient stock'}), 400

    cart_item = ShoppingCart.query.filter_by(user_id=current_user.id, product_id=product_id).first()

    if cart_item:
        cart_item.quantity += quantity
        # db.session.commit()
        # return jsonify({'message': 'Product quantity updated in the cart'}), 200
    else:
        new_cart_item = ShoppingCart(
            user_id=current_user.id,
            product_id=product_id,
            quantity=quantity
        )
        db.session.add(new_cart_item)

    product.stock -= quantity
    db.session.commit()
    return jsonify({'message': 'Product added to the cart'}), 201

@cart_routes.route('/<int:cart_item_id>', methods=['PUT'])
@login_required 
def edit_cart_quantity(cart_item_id):
    """
    Edit the quantity of a product in the logged-in user's cart.
    """
    data = request.get_json()
    new_quantity = int(data.get('quantity'))

    if not new_quantity or new_quantity <= 0:
        return jsonify({'error': 'Invalid quantity'}), 400

    cart_item = ShoppingCart.query.filter_by(id=cart_item_id, user_id=current_user.id).first()

    if not cart_item:
        return jsonify({'error': 'Cart item not found'}), 404

    product = Product.query.get(cart_item.product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    # Calculate the difference between the new quantity and the current quantity
    quantity_difference = new_quantity - cart_item.quantity

    # Check if there's enough stock if the quantity is being increased
    if quantity_difference > 0 and product.stock < quantity_difference:
        return jsonify({'error': 'Insufficient stock for this update'}), 400

    # Update the stock: deduct if increasing cart quantity, add back if decreasing
    product.stock -= quantity_difference
    cart_item.quantity = new_quantity

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

    product = Product.query.get(cart_item.product_id)
    if product:
        product.stock += cart_item.quantity


    db.session.delete(cart_item)
    db.session.commit()

    return jsonify({'message': 'Product removed from cart successfully'}), 200


@cart_routes.route('/checkout', methods=['POST'])
@login_required
def checkout():
    """
    Checkout the items in the user's shopping cart.
    """
    cart_items = ShoppingCart.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        return jsonify({'error': 'Your cart is empty'}), 400

    purchased_items = []

    # Process each item in the cart
    for item in cart_items:
        product = Product.query.get(item.product_id)
        if product:
            purchased_items.append({
                'name': product.name,
                'quantity': item.quantity
            })

            # Remove the item from the cart
            db.session.delete(item)

    # Commit the removal of cart items
    db.session.commit()

    return jsonify({'purchased_items': purchased_items}), 200
