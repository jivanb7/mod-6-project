const LOAD_PRODUCTS = "products/LOAD_PRODUCTS";
const LOAD_PRODUCTS_ERROR = "products/LOAD_PRODUCTS_ERROR";
const LOAD_PRODUCT_DETAIL = "products/LOAD_PRODUCT_DETAIL";
const LOAD_PRODUCT_DETAIL_ERROR = "products/LOAD_PRODUCT_DETAIL_ERROR";
const ADD_PRODUCT = "products/ADD_PRODUCT";
const ADD_PRODUCT_ERROR = "products/ADD_PRODUCT_ERROR";
const LOAD_USER_PRODUCTS = "products/LOAD_USER_PRODUCTS";
const LOAD_USER_PRODUCTS_ERROR = "products/LOAD_USER_PRODUCTS_ERROR";
const UPDATE_PRODUCT = "products/UPDATE_PRODUCT";


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

const addProduct = (product) => ({
  type: ADD_PRODUCT,
  product,
});

const addProductError = (error) => ({
  type: ADD_PRODUCT_ERROR,
  error,
});

const loadUserProducts = (products) => ({
  type: LOAD_USER_PRODUCTS,
  products,
});

const loadUserProductsError = (error) => ({
  type: LOAD_USER_PRODUCTS_ERROR,
  error,
});

const updateProduct = (product) => ({
  type: UPDATE_PRODUCT,
  product,
})

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

export const thunkCreateProduct = (productData) => async (dispatch) => {
  try {
    const response = await fetch("/api/products/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(productData),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || "Failed to create product");
    }

    const newProduct = await response.json();
    dispatch(addProduct(newProduct));
    return newProduct;
  } catch (error) {
    dispatch(addProductError(error.message));
    return { errors: error.message };
  }
};

export const fetchUserInventory = () => async (dispatch) => {
  try {
    const response = await fetch("/api/products/current");
    if (!response.ok) {
      throw new Error("Failed to load user inventory");
    }
    const productsData = await response.json();
    dispatch(loadUserProducts(productsData));
  } catch (error) {
    dispatch(loadUserProductsError(error.message));
  }
};

export const thunkUpdateProduct = (updatedProduct) => async (dispatch) => {
  const response = await fetch(`/api/products/${updatedProduct.id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(updatedProduct),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(updateProduct(data)); // Ensure this action updates the product in Redux state
    return data;
  } else {
    // Handle error
    const errorData = await response.json();
    throw new Error(errorData.error || 'Failed to update product');
  }
};


const initialState = {
  products: [], // <- a list of products (plural)
  userProducts: [],
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
    case LOAD_USER_PRODUCTS:
      return {
        ...state,
        userProducts: action.products,
        error: null,
      };
    case ADD_PRODUCT:
      return {
        ...state,
        products: [...state.products, action.product],
        error: null,
      };
    case UPDATE_PRODUCT:
      return {
        ...state,
        userProducts: state.userProducts.map((p) =>
          p.id === action.product.id ? action.product : p
        ),
        error: null,
      };
    case LOAD_PRODUCTS_ERROR:
    case LOAD_PRODUCT_DETAIL_ERROR:
    case ADD_PRODUCT_ERROR:
    case LOAD_USER_PRODUCTS_ERROR:
      return {
        ...state,
        product: null, 
        error: action.error,
      };

    default:
      return state;
  }
}
