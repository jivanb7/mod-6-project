from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Product, db, Review, User, ProductImage
from app.forms import NewProductForm

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
    Get all the products of the current logged-in user, including preview image.
    """
    products = Product.query.filter_by(user_id=current_user.id).all()
    product_list = []

    for product in products:
        # Retrieve the preview image for the product
        preview_image = ProductImage.query.filter_by(product_id=product.id, preview_image=True).first()
        product_data = product.to_dict()
        if preview_image:
            product_data['preview_image'] = preview_image.image_url  # Add preview image URL
        product_list.append(product_data)

    return jsonify(product_list), 200

@product_routes.route('/<int:product_id>', methods=['GET'])
def get_product_detail(product_id):
    """
    Get the details of a specific product by its ID.
    """
    product = Product.query.get(product_id)

    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    product_data = product.to_dict()

    preview_image = None
    non_preview_images = []
    for image in product.product_images:
        image_data = image.to_dict()
        if image.preview_image:
            preview_image = image_data
        else:
            non_preview_images.append(image_data)

    product_data['preview_image'] = preview_image
    product_data['non_preview_images'] = non_preview_images

    return jsonify(product_data), 200


@product_routes.route('/', methods=['POST'])
@login_required
def create_product():
    """
    Create a new product by the logged-in user.
    """
    form = NewProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        new_product = Product(
            user_id=current_user.id,
            category=form.data['category'],
            name=form.data['name'],
            description=form.data['description'],
            price=form.data['price'],
            stock=form.data['stock']
        )

        # Save product to generate an ID
        db.session.add(new_product)
        db.session.commit()

        # Collect image URLs and add them to ProductImage, marking the first as preview
        image_urls = [form.data[f'image_url{i}'] for i in range(1, 6) if form.data.get(f'image_url{i}')]

        for idx, image_url in enumerate(image_urls):
            product_image = ProductImage(
                product_id=new_product.id,
                image_url=image_url,
                preview_image=(idx == 0)  # Mark the first image as preview
            )
            db.session.add(product_image)

        db.session.commit()

        return jsonify(new_product.to_dict()), 201

    return jsonify(form.errors), 400


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

    # Update product details
    product.category = data.get('category', product.category)
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.stock = data.get('stock', product.stock)

    # Handling images
    image_urls = data.get('images', [])
    if image_urls:
        # Mark only the first image as preview
        preview_image_url = image_urls[0]
        optional_image_urls = image_urls[1:5]  # Up to 4 optional images

        # Clear current images for this product
        ProductImage.query.filter_by(product_id=product_id).delete()

        # Add updated images
        new_images = [
            ProductImage(product_id=product.id, image_url=preview_image_url, preview_image=True)
        ]
        for url in optional_image_urls:
            if url:
                new_images.append(ProductImage(product_id=product.id, image_url=url, preview_image=False))

        db.session.add_all(new_images)

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

    reviews_with_usernames = []
    for review in reviews:
        user = User.query.get(review.user_id)
        review_dict = review.to_dict()
        review_dict['username'] = user.username
        reviews_with_usernames.append(review_dict)

    return jsonify(reviews_with_usernames), 200

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

    # Check if the user has already reviewed this product
    existing_review = Review.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if existing_review:
        return jsonify({'error': 'You have already reviewed this product'}), 400

    data = request.get_json()

    item_quality = data.get('item_quality')
    shipping = data.get('shipping')
    customer_service = data.get('customer_service')
    comment = data.get('comment')
    recommended = data.get('recommended')

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
        recommended=recommended
    )

    db.session.add(new_review)
    db.session.commit()

    return jsonify(new_review.to_dict()), 201

