const ADD_TO_CART_REQUEST = 'ADD_TO_CART_REQUEST';
const ADD_TO_CART_SUCCESS = 'ADD_TO_CART_SUCCESS';
const ADD_TO_CART_FAILURE = 'ADD_TO_CART_FAILURE';
const GET_CART_TOTAL_REQUEST = 'GET_CART_TOTAL_REQUEST';
const GET_CART_TOTAL_SUCCESS = 'GET_CART_TOTAL_SUCCESS';
const GET_CART_TOTAL_FAILURE = 'GET_CART_TOTAL_FAILURE';
const REMOVE_FROM_CART_REQUEST = 'REMOVE_FROM_CART_REQUEST';
const REMOVE_FROM_CART_SUCCESS = 'REMOVE_FROM_CART_SUCCESS';
const REMOVE_FROM_CART_FAILURE = 'REMOVE_FROM_CART_FAILURE';
const UPDATE_CART_ITEM_REQUEST = 'UPDATE_CART_ITEM_REQUEST';
const UPDATE_CART_ITEM_SUCCESS = 'UPDATE_CART_ITEM_SUCCESS';
const UPDATE_CART_ITEM_FAILURE = 'UPDATE_CART_ITEM_FAILURE';

const addToCartRequest = () => ({ type: ADD_TO_CART_REQUEST });
const addToCartSuccess = (item) => ({ type: ADD_TO_CART_SUCCESS, payload: item });
const addToCartFailure = (error) => ({ type: ADD_TO_CART_FAILURE, payload: error });
const getCartTotalRequest = () => ({ type: GET_CART_TOTAL_REQUEST });
const getCartTotalSuccess = (total) => ({ type: GET_CART_TOTAL_SUCCESS, payload: total });
const getCartTotalFailure = (error) => ({ type: GET_CART_TOTAL_FAILURE, payload: error });
const removeFromCartRequest = () => ({ type: REMOVE_FROM_CART_REQUEST });
const removeFromCartSuccess = (itemId) => ({ type: REMOVE_FROM_CART_SUCCESS, payload: itemId });
const removeFromCartFailure = (error) => ({ type: REMOVE_FROM_CART_FAILURE, payload: error });
const updateCartItemRequest = () => ({ type: UPDATE_CART_ITEM_REQUEST });
const updateCartItemSuccess = (item) => ({ type: UPDATE_CART_ITEM_SUCCESS, payload: item });
const updateCartItemFailure = (error) => ({ type: UPDATE_CART_ITEM_FAILURE, payload: error });



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
    dispatch(fetchCartTotal());
  } catch (error) {
    dispatch(addToCartFailure(error.message));
  }
};

export const fetchCartTotal = () => async (dispatch) => {
  dispatch(getCartTotalRequest());
  try {
    const response = await fetch('/api/cart/total', {
      method: 'GET',
    });
    if (!response.ok) {
      throw new Error('Failed to fetch cart total');
    }
    const data = await response.json();
    dispatch(getCartTotalSuccess(data.total_items));
  } catch (error) {
    dispatch(getCartTotalFailure(error.message));
  }
};

export const removeFromCart = (itemId) => async (dispatch) => {
  dispatch(removeFromCartRequest());
  try {
    const response = await fetch(`/api/cart/${itemId}`, {
      method: 'DELETE',
    });
    if (!response.ok) {
      throw new Error('Failed to remove item from cart');
    }
    dispatch(removeFromCartSuccess(itemId));
    dispatch(fetchCartTotal());
  } catch (error) {
    dispatch(removeFromCartFailure(error.message));
  }
};

export const updateCartItem = (itemId, quantity) => async (dispatch) => {
  dispatch(updateCartItemRequest());
  try {
    const response = await fetch(`/api/cart/${itemId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ quantity }),
    });
    if (!response.ok) {
      throw new Error('Failed to update cart item');
    }
    const data = await response.json();
    dispatch(updateCartItemSuccess(data));
    dispatch(fetchCartTotal());
  } catch (error) {
    dispatch(updateCartItemFailure(error.message));
  }
};



const initialState = {
  items: [],
  totalItems: 0,
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
    case GET_CART_TOTAL_REQUEST:
      return { ...state, loading: true, error: null };
    case GET_CART_TOTAL_SUCCESS:
      return { ...state, loading: false, totalItems: action.payload };
    case GET_CART_TOTAL_FAILURE:
      return { ...state, loading: false, error: action.payload };
    case REMOVE_FROM_CART_REQUEST:
    case UPDATE_CART_ITEM_REQUEST:
      return { ...state, loading: true, error: null };
    case REMOVE_FROM_CART_SUCCESS:
      return {
        ...state,
        loading: false,
        items: state.items.filter((item) => item.id !== action.payload),
      };
    case UPDATE_CART_ITEM_SUCCESS:
      return {
        ...state,
        loading: false,
        items: state.items.map((item) =>
          item.id === action.payload.id ? action.payload : item
        ),
      };
    case REMOVE_FROM_CART_FAILURE:
    case UPDATE_CART_ITEM_FAILURE:
      return { ...state, loading: false, error: action.payload };

    default:
      return state;
  }
}
