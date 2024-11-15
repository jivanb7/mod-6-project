from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Review, db

review_routes = Blueprint('reviews', __name__)

@review_routes.route('/current', methods=['GET'])
@login_required 
def get_current_user_reviews():
    """
    Get all reviews made by the current logged-in user.
    """
    reviews = Review.query.filter_by(user_id=current_user.id).all()

    if not reviews:
        return jsonify({'message': 'No reviews found'}), 200

    return jsonify([review.to_dict() for review in reviews]), 200

@review_routes.route('/<int:review_id>', methods=['PUT'])
@login_required
def edit_review(review_id):
    """
    Edit the review created by the current logged-in user.
    Only the review owner can edit it.
    """
    review = Review.query.get(review_id)
    
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    
    if review.user_id != current_user.id:
        return jsonify({'error': 'You are not authorized to edit this review'}), 403
    
    data = request.get_json()

    if 'item_quality' in data:
        review.item_quality = data['item_quality']
    if 'shipping' in data:
        review.shipping = data['shipping']
    if 'customer_service' in data:
        review.customer_service = data['customer_service']
    if 'comment' in data:
        review.comment = data['comment']
    if 'recommended' in data:
        review.recommended = data['recommended']

    if any(rating < 1 or rating > 5 for rating in [review.item_quality, review.shipping, review.customer_service]):
        return jsonify({'error': 'All ratings must be between 1 and 5'}), 400
    
    rating = round((review.item_quality + review.shipping + review.customer_service) / 3)
    review.rating = rating

    db.session.commit()

    return jsonify(review.to_dict()), 200

@review_routes.route('/<int:review_id>', methods=['DELETE'])
@login_required
def delete_review(review_id):
    """
    Delete a review created by the current logged-in user.
    """
    review = Review.query.get(review_id)
    
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    
    if review.user_id != current_user.id:
        return jsonify({'error': 'You are not authorized to delete this review'}), 403
    
    db.session.delete(review)
    db.session.commit()

    return jsonify({'message': 'Review deleted successfully'}), 200
