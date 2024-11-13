const LOAD_PRODUCT_DETAIL = "products/LOAD_PRODUCT_DETAIL";
const LOAD_PRODUCT_DETAIL_ERROR = "products/LOAD_PRODUCT_DETAIL_ERROR";

const loadProductDetail = (product) => ({
  type: LOAD_PRODUCT_DETAIL,
  product,
});

const loadProductDetailError = (error) => ({
  type: LOAD_PRODUCT_DETAIL_ERROR,
  error,
});

export const fetchProductDetail = (product_id) => async (dispatch) => {
  try {
    const response = await fetch(`/api/products/${product_id}`);
    if (!response.ok) {
      throw new Error("Product not found");
    }
    const productData = await response.json();
    dispatch(loadProductDetail(productData));
  } catch (error) {
    dispatch(loadProductDetailError(error.message));
  }
};

const initialState = {
  product: null,
  error: null, 
};

export default function productsReducer(state = initialState, action) {
  switch (action.type) {
    case LOAD_PRODUCT_DETAIL:
      return {
        ...state,
        product: action.product,
        error: null, 
      };

    case LOAD_PRODUCT_DETAIL_ERROR:
      return {
        ...state,
        product: null, 
        error: action.error,
      };

    default:
      return state;
  }
}
