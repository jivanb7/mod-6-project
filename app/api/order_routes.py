from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import Order

order_routes = Blueprint('orders', __name__)


@order_routes.route('/current', methods=['GET'])
@login_required
def get_user_orders():
    """
    Get all orders for the logged-in user.
    """
    orders = Order.query.filter_by(user_id=current_user.id).all()

    if not orders:
        return jsonify({'message': 'No orders found for the current user'}), 200

    order_list = [order.to_dict() for order in orders]

    return jsonify({'orders': order_list}), 200
