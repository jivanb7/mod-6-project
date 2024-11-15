const ADD_FAVORITE = "ADD_FAVORITE";
const REMOVE_FAVORITE = "REMOVE_FAVORITE";
const SET_FAVORITES = "SET_FAVORITES";
const FAVORITE_ERROR = "FAVORITE_ERROR";

const addFavorite = (favorite) => ({
  type: ADD_FAVORITE,
  favorite,
});

const removeFavorite = (productId) => ({
  type: REMOVE_FAVORITE,
  productId,
});

const setFavorites = (favorites) => ({
  type: SET_FAVORITES,
  favorites,
});

const favoriteError = (error) => ({
  type: FAVORITE_ERROR,
  error,
});

export const fetchFavorites = () => async (dispatch) => {
  try {
    const response = await fetch("/api/favorites/current", {
      method: "GET",
    });

    if (!response.ok) {
      throw new Error("Failed to fetch favorites");
    }

    const favorites = await response.json();
    dispatch(setFavorites(favorites)); 
  } catch (error) {
    dispatch(favoriteError(error.message));
  }
};

export const addToFavorites = (productId) => async (dispatch) => {
  try {
    const response = await fetch(`/api/favorites/${productId}`, {
      method: "POST",
    });

    if (!response.ok) {
      throw new Error("Failed to add to favorites");
    }

    const newFavorite = await response.json();
    dispatch(addFavorite(newFavorite));
  } catch (error) {
    dispatch(favoriteError(error.message));
  }
};

export const removeFromFavorites = (productId) => async (dispatch) => {
  try {
    const response = await fetch(`/api/favorites/${productId}`, {
      method: "DELETE",
    });

    if (!response.ok) {
      throw new Error("Failed to remove from favorites");
    }

    dispatch(removeFavorite(productId)); 
  } catch (error) {
    dispatch(favoriteError(error.message));
  }
};

const initialState = {
  favorites: [], 
  error: null, 
};

export default function favoriteReducer(state = initialState, action) {
  switch (action.type) {
    case ADD_FAVORITE:
      return {
        ...state,
        favorites: [...state.favorites, action.favorite],
        error: null,
      };
    case REMOVE_FAVORITE:
      return {
        ...state,
        favorites: state.favorites.filter((favorite) => favorite.product_id !== action.productId),
        error: null,
      };
    case SET_FAVORITES:
      return {
        ...state,
        favorites: action.favorites,
        error: null,
      };
    case FAVORITE_ERROR:
      return {
        ...state,
        error: action.error, 
      };
    default:
      return state;
  }
}
