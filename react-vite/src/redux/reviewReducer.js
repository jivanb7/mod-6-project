const LOAD_REVIEWS = "LOAD_REVIEWS";
const LOAD_REVIEWS_ERROR = "LOAD_REVIEWS_ERROR";
const POST_REVIEW = "POST_REVIEW";
const POST_REVIEW_ERROR = "POST_REVIEW_ERROR";
const UPDATE_REVIEW = "UPDATE_REVIEW";
const UPDATE_REVIEW_ERROR = "UPDATE_REVIEW_ERROR";
const DELETE_REVIEW = "DELETE_REVIEW";
const DELETE_REVIEW_ERROR = "DELETE_REVIEW_ERROR";

const loadReviews = (reviews) => ({
  type: LOAD_REVIEWS,
  reviews,
});

const loadReviewsError = (error) => ({
  type: LOAD_REVIEWS_ERROR,
  error,
});

const addReview = (review) => ({
  type: POST_REVIEW,
  review,
});

const addReviewError = (error) => ({
  type: POST_REVIEW_ERROR,
  error,
});

const updateReview = (review) => ({
  type: UPDATE_REVIEW,
  review,
});

const updateReviewError = (error) => ({
  type: UPDATE_REVIEW_ERROR,
  error,
});

const deleteReview = (reviewId) => ({
  type: DELETE_REVIEW,
  reviewId,
});

const deleteReviewError = (error) => ({
  type: DELETE_REVIEW_ERROR,
  error,
});

export const fetchProductReviews = (product_id) => async (dispatch) => {
  try {
    const response = await fetch(`/api/products/${product_id}/reviews`);
    if (!response.ok) {
      throw new Error("Reviews not found");
    }
    const reviewsData = await response.json();
    dispatch(loadReviews(reviewsData));
  } catch (error) {
    dispatch(loadReviewsError(error.message));
  }
};

export const postProductReview = (product_id, reviewData) => async (dispatch) => {
  try {
    const response = await fetch(`/api/products/${product_id}/reviews`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(reviewData),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to post review');
    }

    const newReview = await response.json();
    dispatch(addReview(newReview));
    return newReview;
  } catch (error) {
    dispatch(addReviewError(error.message));
    return { error: error.message };
  }
};

export const updateProductReview = (review_id, updatedData) => async (dispatch) => {
  try {
    const response = await fetch(`/api/reviews/${review_id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(updatedData),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to update review');
    }

    const updatedReview = await response.json();
    dispatch(updateReview(updatedReview));
    return updatedReview;
  } catch (error) {
    dispatch(updateReviewError(error.message));
    return { error: error.message };
  }
};

export const deleteProductReview = (reviewId) => async (dispatch) => {
  try {
    const response = await fetch(`/api/reviews/${reviewId}`, {
      method: 'DELETE',
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'Failed to delete review');
    }

    dispatch(deleteReview(reviewId));
  } catch (error) {
    dispatch(deleteReviewError(error.message));
  }
};

const initialState = {
  reviews: [],
  error: null,
  postError: null,
  updateError: null,
  deleteError: null,
};

export default function reviewReducer(state = initialState, action) {
  switch (action.type) {
    case LOAD_REVIEWS:
      return {
        ...state,
        reviews: action.reviews,
        error: null,
      };
    case LOAD_REVIEWS_ERROR:
      return {
        ...state,
        reviews: [],
        error: action.error,
      };
    case POST_REVIEW:
      return {
        ...state,
        reviews: [...state.reviews, action.review],
        postError: null,
      };
    case POST_REVIEW_ERROR:
      return {
        ...state,
        postError: action.error,
      };
    case UPDATE_REVIEW:
      return {
        ...state,
        reviews: state.reviews.map((review) =>
          review.id === action.review.id ? action.review : review
        ),
        updateError: null,
      };
    case UPDATE_REVIEW_ERROR:
      return {
        ...state,
        updateError: action.error,
      };
    case DELETE_REVIEW:
      return {
        ...state,
        reviews: state.reviews.filter((review) => review.id !== action.reviewId),
        deleteError: null,
      };
    case DELETE_REVIEW_ERROR:
      return {
        ...state,
        deleteError: action.error,
      };
    default:
      return state;
  }
}
