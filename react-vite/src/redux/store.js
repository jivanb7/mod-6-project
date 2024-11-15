import {
  legacy_createStore as createStore,
  applyMiddleware,
  compose,
  combineReducers,
} from "redux";
import thunk from "redux-thunk";
import sessionReducer from "./session";
import productsReducer from "./productReducer";
import reviewReducer from "./reviewReducer";
import cartReducer from "./cartReducer";
import favoriteReducer from "./favoriteReducer";

const rootReducer = combineReducers({
  session: sessionReducer,
  products: productsReducer,
  reviews: reviewReducer,
  carts: cartReducer,
  favorites: favoriteReducer,
});

let enhancer;
if (import.meta.env.MODE === "production") {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = (await import("redux-logger")).default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
