import {useEffect, useState} from "react";
import {useDispatch, useSelector} from "react-redux";
import {Link, useParams} from "react-router-dom";
import {fetchProductDetail} from "../../redux/productReducer";
import {fetchProductReviews} from "../../redux/reviewReducer";
import {addToCart} from "../../redux/cartReducer";
import {addToFavorites, fetchFavorites, removeFromFavorites} from "../../redux/favoriteReducer"
import {FaStar} from "react-icons/fa";
import {FaCheck} from "react-icons/fa6";
import {FaHeart, FaRegHeart} from "react-icons/fa";
import './ProductDetail.css';
import OpenModalButton from "../OpenModalButton/OpenModalButton";
import ReviewFormModal from "../ReviewFormModal/ReviewFormModal";
import DeleteReviewModal from "../DeleteReviewModal/DeleteReviewModal";
import {fetchAllProducts} from "../../redux/productReducer.js";

function ProductDetail()
{
  const dispatch = useDispatch();
  const {product_id} = useParams();

  const product = useSelector((state) => state.products.product);
  const productError = useSelector((state) => state.products.error);
  const reviews = useSelector((state) => state.reviews.reviews);
  const currentUser = useSelector((state) => state.session.user);
  const favorites = useSelector((state) => state.favorites.favorites);

  const [selectedImage, setSelectedImage] = useState(product?.preview_image);
  const [localIsFavorited, setLocalIsFavorited] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const isOwner = currentUser && currentUser.id === product?.user_id;
  const isLoggedIn = Boolean(currentUser);
  const userReview = reviews.find((review) => review.user_id === currentUser?.id);
  const nonPreviewImages = product?.non_preview_images || [];

  const handleAddToCart = async () => {
    await dispatch(addToCart(product_id));
    dispatch(fetchProductDetail(product_id));
    dispatch(fetchAllProducts());
  };

  useEffect(() => {
    if (currentUser) {
      dispatch(fetchFavorites());
    }
  }, [dispatch, currentUser]);

  useEffect(() => {
    if (favorites && product_id) {
      const isFavorited = favorites.some((favorite) => favorite.product_id === Number(product_id));
      setLocalIsFavorited(isFavorited);
    }
  }, [favorites, product_id]);

  const handleFavoriteToggle = async () => {
    const optimisticState = !localIsFavorited;
    setLocalIsFavorited(optimisticState);
    setIsLoading(true);


    try {
      if (optimisticState) {
        await dispatch(addToFavorites(product_id));
      } else {
        await dispatch(removeFromFavorites(product_id));
      }
      await dispatch(fetchFavorites());

    } catch (error) {
      console.error("Error updating favorites:", error);
      setLocalIsFavorited(!optimisticState);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    if (product && product.preview_image) {
      setSelectedImage(product.preview_image);
    }
  }, [product]);

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
          <div className="thumbnail-column">
            {[product.preview_image, ...nonPreviewImages].map((image) => (
              <img
                key={image.id}
                src={image.image_url}
                alt={`${product.name} thumbnail`}
                className="thumbnail"
                onClick={() => setSelectedImage(image)}
              />
            ))}
          </div>
          <div className="main-image">
            {selectedImage && (
              <img className="bigimg" src={selectedImage.image_url} alt={product.name}/>
            )}
          </div>
        </div>
        <div className="prodinfo">
          <div className="prodinfoinside">
            <div className="prodnameheart">
              <h1>{product.name}</h1>


              {!isOwner && currentUser && (
                <button
                  onClick={handleFavoriteToggle}
                  className="favorite-button"
                  disabled={isLoading}
                >
                  {localIsFavorited ? (
                    <FaHeart style={{width: "24px", color: "red"}}/>
                  ) : (
                    <FaRegHeart style={{width: "24px", color: "gray"}}/>
                  )}
                </button>
              )}

            </div>


            <h4>Sold By {product.username}</h4>
            <p>{product.description}</p>
          </div>
          <div className="prodpricenumcart">
            <p className="prodpricenum">Current Price : ${product.price}</p>
            <p className="prodpricenum"> Quantity available : {product.stock} </p>
            {isOwner && (
              <div className="owner-of-product">
                <p>You own this product</p>
                <Link to="/inventory">
                  <button>
                    Manage your inventory
                  </button>
                </Link>
              </div>)
            }
            {!isOwner && currentUser && (
              <div className="buttondiv">
                <button className="cartbutton" onClick={handleAddToCart} disabled={product.stock === 0}>Add to Cart
                </button>
              </div>
            )}
            {!currentUser &&
              <div className="buttondiv">
              <p>Create an account or login to add items to your cart</p>
              </div>}
          < /div>
        </div>
      </div>

      <div className="review-detail">
        <h2 className="review-h2">{reviews.length} Reviews <FaStar/></h2>

        <div>
          {isLoggedIn && !isOwner && !userReview && (
            <OpenModalButton
              modalComponent={<ReviewFormModal productId={product_id}/>}
              buttonText="Post a Review"
              style={{borderRadius: "5px", backgroundColor: "green", color: "white", cursor: "pointer"}}
            />
          )}
          {!isLoggedIn && (
            <p>Create an Account to leave a Review!</p>
          )}
        </div>

        {reviews.length > 0 && (
          <div>
            {reviews.map((review) => (
              <div key={review.id} className="review-container">
                <div className="revstarall">
                  <div className="revstar-comment">
                    <p> {renderStars(review.rating)} </p>
                    <p className="revcomment"> {review.comment} </p>
                    <div className="revuseranddate">
                      <p className="revuser"> {review.username} </p>
                      <p className="revdate">{new Date(review.created_at).toLocaleDateString("en-US", {
                        month: "short",
                        day: "numeric",
                        year: "numeric"
                      })}</p>
                    </div>
                  </div>
                  <div className="revstarinfo">
                    {review.recommended && (
                      <p className="recommended"><FaCheck color="#228B22"/> Recommended this item</p>)}
                    <p><strong>Item Quality:</strong> {review.item_quality} <FaStar/></p>
                    <p><strong>Shipping:</strong> {review.shipping} <FaStar/></p>
                    <p><strong>Customer Service:</strong> {review.customer_service} <FaStar/></p>
                  </div>
                </div>

                {isLoggedIn && review.user_id === currentUser?.id && (
                  <div className="managebuttons">
                    <OpenModalButton
                      modalComponent={<ReviewFormModal productId={product_id} reviewData={review}/>}
                      buttonText="Update Review"
                      style={{borderRadius: "5px", backgroundColor: "green", color: "white", cursor: "pointer"}}
                    />
                    <OpenModalButton
                      modalComponent={<DeleteReviewModal reviewId={review.id}/>}
                      buttonText="Delete Review"
                      style={{borderRadius: "5px", backgroundColor: "green", color: "white", cursor: "pointer"}}
                    />
                  </div>
                )}
              </div>
            ))}
          </div>
        )}
        {reviews.length === 0 && !isOwner && currentUser && <p>Be the first to post a review!</p>}
        {reviews.length === 0 && isOwner && currentUser && <p>No reviews for your product.</p> }
      </div>
    </div>
  );
}

export default ProductDetail;