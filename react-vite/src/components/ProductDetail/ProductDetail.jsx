import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { fetchProductDetail } from "../../redux/productReducer";
import { fetchProductReviews } from "../../redux/reviewReducer";
import { FaStar } from "react-icons/fa";
import './ProductDetail.css';
import OpenModalButton from "../OpenModalButton/OpenModalButton";
import ReviewFormModal from "../ReviewFormModal/ReviewFormModal";
import DeleteReviewModal from "../DeleteReviewModal/DeleteReviewModal";

function ProductDetail() {
  const dispatch = useDispatch();
  const { product_id } = useParams();

  const product = useSelector((state) => state.products.product);
  const productError = useSelector((state) => state.products.error);
  const reviews = useSelector((state) => state.reviews.reviews);
  const currentUser = useSelector((state) => state.session.user);

  const isOwner = currentUser && currentUser.id === product?.user_id;
  const isLoggedIn = Boolean(currentUser);
  const userReview = reviews.find((review) => review.user_id === currentUser?.id);

  useEffect(() => {
    dispatch(fetchProductDetail(product_id));
    dispatch(fetchProductReviews(product_id));
  }, [dispatch, product_id]);

  if (productError) {
    return <div>{productError}</div>;
  }

  if (!product) {
    return;
  }

  const renderStars = (rating) => {
    let stars = [];
    for (let i = 1; i <= 5; i++) {
      stars.push(
        <FaStar
          key={i}
          color={i <= rating ? "black" : "white"}
          size={20}
        />
      );
    }
    return stars;
  };

  return (
    <div>
      <div className="product-detail">
        <div className="prodimage">
          {product.preview_image && (
            <img src={product.preview_image.image_url} alt={product.name} />
          )}
        </div>
        <div className="prodinfo">
          <h1>{product.name}</h1>
          <p>{product.description}</p>
          <p>Price: ${product.price}</p>
          <p>Stock: {product.stock} available</p>
        </div>
      </div>

      <div className="review-detail">
        <h2>{reviews.length} Reviews <FaStar /></h2>

        <div>
          {isLoggedIn && !isOwner && !userReview && (
            <OpenModalButton
              modalComponent={<ReviewFormModal productId={product_id} />}
              buttonText="Post a Review"
            />
          )}
          {!isLoggedIn && (
            <p>Log in to post a review!</p>
          )}
        </div>

        {reviews.length > 0 ? (
          <div>
            {reviews.map((review) => (
              <div key={review.id} className="review-container">
                <div className="revstarall">
                  <div className="revstar-comment">
                    <p> {renderStars(review.rating)} </p>
                    <p> {review.comment} </p>
                    <p> {review.username} {new Date(review.created_at).toLocaleDateString()}</p>
                  </div>
                  <div className="revstarinfo">
                    {review.recommended && (<p><strong>Recommended:</strong> Yes</p>)}
                    <p><strong>Item Quality:</strong> {review.item_quality} <FaStar /> </p>
                    <p><strong>Shipping:</strong> {review.shipping} <FaStar /> </p>
                    <p><strong>Customer Service:</strong> {review.customer_service} <FaStar /> </p>
                  </div>
                </div>

                {isLoggedIn && review.user_id === currentUser?.id && (
                  <div>
                  <OpenModalButton
                    modalComponent={<ReviewFormModal productId={product_id} reviewData={review} />}
                    buttonText="Update Review"
                  />
                  <OpenModalButton
                    modalComponent={<DeleteReviewModal reviewId={review.id} />}
                    buttonText="Delete Review"
                  />
                  </div>
                )}
              </div>
            ))}
          </div>
        ) : (
          <p>Be the first to post a review!</p>
        )}
      </div>
    </div>
  );
}

export default ProductDetail;
