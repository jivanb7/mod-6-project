from flask import Blueprint, request, jsonify
from app.models import User, db, Favorite, Product
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': {'message': 'Unauthorized'}}, 401


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Add the user to the session, we are logged in!
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        return user.to_dict()
    return form.errors, 401


@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password']
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return user.to_dict()
    return form.errors, 401


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': {'message': 'Unauthorized'}}, 401

@auth_routes.route('/favorites', methods=['GET'])
@login_required
def get_favorites():
    """
    Get all the favorite products for the logged-in user.
    """
    favorites = Favorite.query.filter_by(user_id=current_user.id).all()

    favorite_products = []
    for favorite in favorites:
        product = Product.query.get(favorite.product_id)
        if product: 
            favorite_products.append(product.to_dict())
    
    return jsonify(favorite_products), 200

@auth_routes.route('/favorites', methods=['POST'])
@login_required
def add_favorite():
    """
    Add a product to the logged-in user's favorites.
    """
    data = request.get_json()
    product_id = data.get('product_id')

    new_favorite = Favorite(user_id=current_user.id, product_id=product_id)
    db.session.add(new_favorite)
    db.session.commit()

    return jsonify({'message': 'Product added to favorites'}), 201

@auth_routes.route('/favorites/<int:product_id>', methods=['DELETE'])
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