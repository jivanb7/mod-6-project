const ADD_TO_CART_REQUEST = 'ADD_TO_CART_REQUEST';
const ADD_TO_CART_SUCCESS = 'ADD_TO_CART_SUCCESS';
const ADD_TO_CART_FAILURE = 'ADD_TO_CART_FAILURE';

const addToCartRequest = () => ({ type: ADD_TO_CART_REQUEST });
const addToCartSuccess = (item) => ({ type: ADD_TO_CART_SUCCESS, payload: item });
const addToCartFailure = (error) => ({ type: ADD_TO_CART_FAILURE, payload: error });

export const addToCart = (productId, quantity = 1) => async (dispatch) => {
  dispatch(addToCartRequest());
  try {
    const response = await fetch('/api/cart/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ product_id: productId, quantity }),
    });
    if (!response.ok) {
      throw new Error('Failed to add item to cart');
    }
    const data = await response.json();
    dispatch(addToCartSuccess(data));
  } catch (error) {
    dispatch(addToCartFailure(error.message));
  }
};

const initialState = {
  items: [],
  loading: false,
  error: null,
};

export default function cartReducer(state = initialState, action) {
  switch (action.type) {
    case ADD_TO_CART_REQUEST:
      return { ...state, loading: true, error: null };
    case ADD_TO_CART_SUCCESS:
      return { ...state, loading: false, items: [...state.items, action.payload] };
    case ADD_TO_CART_FAILURE:
      return { ...state, loading: false, error: action.payload };
    default:
      return state;
  }
}
