import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { fetchProductReviews, postProductReview, updateProductReview } from '../../redux/reviewReducer';
import { FaStar } from "react-icons/fa";
import { useModal } from '../../context/Modal';

const ReviewFormModal = ({ productId, reviewData }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    const [itemQuality, setItemQuality] = useState(reviewData?.item_quality || 0);
    const [shipping, setShipping] = useState(reviewData?.shipping || 0);
    const [customerService, setCustomerService] = useState(reviewData?.customer_service || 0);
    const [comment, setComment] = useState(reviewData?.comment || '');
    const [recommended, setRecommended] = useState(reviewData?.recommended || false); 
    const [errors, setErrors] = useState([]);

    const [hoverItemQuality, setHoverItemQuality] = useState(0);
    const [hoverShipping, setHoverShipping] = useState(0);
    const [hoverCustomerService, setHoverCustomerService] = useState(0);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const validationErrors = [];

        if (!itemQuality || !shipping || !customerService) {
            validationErrors.push('All ratings must be between 1 and 5.');
        }
        if (comment.length < 10) {
            validationErrors.push('Comment must be at least 10 characters.');
        }

        if (validationErrors.length > 0) {
            setErrors(validationErrors);
            return;
        }

        const reviewPayload = {
            item_quality: itemQuality,
            shipping,
            customer_service: customerService,
            comment,
            recommended,
        };

        let result;
        if (reviewData) {
            result = await dispatch(updateProductReview(reviewData.id, reviewPayload));
        } else {
            result = await dispatch(postProductReview(productId, reviewPayload));
        }

        if (result && !result.error) {
            await dispatch(fetchProductReviews(productId));
            closeModal();
        } else {
            setErrors([result.error || 'Failed to submit review.']);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="review-form">
            <h2 style={{ textAlign: "center" }}>{reviewData ? 'Update Your Review' : 'Post Your Review'}</h2>
            {errors.length > 0 && (
                <div className="error-messages">
                    {errors.map((error, idx) => (
                        <div style={{ color: "red" }} key={idx}>{error}</div>
                    ))}
                </div>
            )}

            <div style={{ margin: '10px 0' }}>
                <label><strong>Item Quality:</strong></label>
                <div>
                    {[1, 2, 3, 4, 5].map((star) => (
                        <span
                            key={star}
                            onMouseEnter={() => setHoverItemQuality(star)}
                            onMouseLeave={() => setHoverItemQuality(0)}
                            onClick={() => setItemQuality(star)}
                        >
                            <FaStar
                                size={30}
                                color={star <= (hoverItemQuality || itemQuality) ? "#ffc107" : "#e4e5e9"}
                                style={{ cursor: "pointer" }}
                            />
                        </span>
                    ))}
                </div>
            </div>

            <div style={{ margin: '10px 0' }}>
                <label><strong>Shipping:</strong></label>
                <div>
                    {[1, 2, 3, 4, 5].map((star) => (
                        <span
                            key={star}
                            onMouseEnter={() => setHoverShipping(star)}
                            onMouseLeave={() => setHoverShipping(0)}
                            onClick={() => setShipping(star)}
                        >
                            <FaStar
                                size={30}
                                color={star <= (hoverShipping || shipping) ? "#ffc107" : "#e4e5e9"}
                                style={{ cursor: "pointer" }}
                            />
                        </span>
                    ))}
                </div>
            </div>

            <div style={{ margin: '10px 0' }}>
                <label><strong>Customer Service:</strong></label>
                <div>
                    {[1, 2, 3, 4, 5].map((star) => (
                        <span
                            key={star}
                            onMouseEnter={() => setHoverCustomerService(star)}
                            onMouseLeave={() => setHoverCustomerService(0)}
                            onClick={() => setCustomerService(star)}
                        >
                            <FaStar
                                size={30}
                                color={star <= (hoverCustomerService || customerService) ? "#ffc107" : "#e4e5e9"}
                                style={{ cursor: "pointer" }}
                            />
                        </span>
                    ))}
                </div>
            </div>

            <div style={{ margin: '10px 0' }}>
                <textarea
                    value={comment}
                    onChange={(e) => setComment(e.target.value)}
                    placeholder="Leave your comment here..."
                    style={{ width: '100%', height: '100px' }}
                />
            </div>

            <div style={{ margin: '10px 0' }}>
                <label><strong>Would you recommend this product?</strong></label>
                <div>
                    <label>
                        <input
                            type="radio"
                            name="recommended"
                            value="yes"
                            checked={recommended === true}
                            onChange={() => setRecommended(true)}
                        />
                        Yes
                    </label>
                    <label style={{ marginLeft: '20px' }}>
                        <input
                            type="radio"
                            name="recommended"
                            value="no"
                            checked={recommended === false}
                            onChange={() => setRecommended(false)}
                        />
                        No
                    </label>
                </div>
            </div>

            <button type="submit" style={{ backgroundColor: "blue", color: "white", padding: '10px', border: 'none', borderRadius: '5px' }}>
                {reviewData ? 'Update Review' : 'Submit Review'}
            </button>
        </form>
    );
};

export default ReviewFormModal;
