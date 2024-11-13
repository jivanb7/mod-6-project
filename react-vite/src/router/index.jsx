import { createBrowserRouter } from 'react-router-dom';
import LandingPage from '../components/LandingPage'
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import ProductDetail from '../components/ProductDetail/ProductDetail';
import Layout from './Layout';

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
        path: "/product/:product_id",
        element: <ProductDetail />
      },
    ],
  },
]);