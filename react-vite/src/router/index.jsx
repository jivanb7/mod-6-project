import { createBrowserRouter } from 'react-router-dom';
import LandingPage from '../components/LandingPage'
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import FavoritesPage from '../components/FavoritesPage';
import ProductsPage from '../components/ProductsPage';
import ProductDetail from '../components/ProductDetail/ProductDetail';
import Layout from './Layout';
import ShoppingCartPage from "../components/ShoppingCartPage/index.js";
import OrderHistoryPage from "../components/OrderHistoryPage/index.js";
import CreateNewProductPage from "../components/CreateNewProductPage/index.js";
import UserInventoryPage from "../components/UserInventoryPage/index.js";

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <LandingPage />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "favorites",
        element: <FavoritesPage />

      },
      {
        path: "/product",
        element: <ProductsPage />,
      },
      {
        path: "shopping-cart",
        element: <ShoppingCartPage />
      },
      {
        path: "/product/:product_id",
        element: <ProductDetail />
      },
      {
        path: "orders",
        element: <OrderHistoryPage />
      },
      {
        path: "create-product",
        element: <CreateNewProductPage />
      },
      {
        path: "inventory",
        element: <UserInventoryPage />
      }
    ],
  },
]);