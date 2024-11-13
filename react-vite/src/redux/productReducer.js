const LOAD_PRODUCTS = "products/LOAD_PRODUCTS";
const LOAD_PRODUCTS_ERROR = "products/LOAD_PRODUCTS_ERROR";
const LOAD_PRODUCT_DETAIL = "products/LOAD_PRODUCT_DETAIL";
const LOAD_PRODUCT_DETAIL_ERROR = "products/LOAD_PRODUCT_DETAIL_ERROR";

const loadProducts = (products) => ({
  type: LOAD_PRODUCTS,
  products,
});

const loadProductsError = (error) => ({
  type: LOAD_PRODUCTS_ERROR,
  error,
});

const loadProductDetail = (product) => ({
  type: LOAD_PRODUCT_DETAIL,
  product,
});

const loadProductDetailError = (error) => ({
  type: LOAD_PRODUCT_DETAIL_ERROR,
  error,
});

export const fetchAllProducts = () => async (dispatch) => {
  try {
    const response = await fetch('/api/products');
    if (!response.ok) {
      throw new Error("Failed to load products");
    }
    const productsData = await response.json();
    dispatch(loadProducts(productsData));
  } catch (error) {
    dispatch(loadProductsError(error.message));
  }
};

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
  products: [], // <- a list of products (plural)
  product: null, // <- just a single product
  error: null, 
};

export default function productsReducer(state = initialState, action) {
  switch (action.type) {

    case LOAD_PRODUCTS:
      return {
        ...state,
        products: action.products,
        error: null,
      };

    case LOAD_PRODUCT_DETAIL:
      return {
        ...state,
        product: action.product,
        error: null, 
      };

    case LOAD_PRODUCTS_ERROR:
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
