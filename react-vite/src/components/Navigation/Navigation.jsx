import ProfileButton from "./ProfileButton";
import {useDispatch, useSelector} from "react-redux";
import {Link} from "react-router-dom";
import {PiShoppingCartSimple, PiHeartBold} from "react-icons/pi";
import "./Navigation.css";
import {useEffect} from "react";
import {fetchCartTotal} from "../../redux/cartReducer.js";

function Navigation()
{
  const sessionUser = useSelector(state => state.session.user);
  const totalItems = useSelector((state) => state.cart.totalItems);
  const dispatch = useDispatch();


  useEffect(() => {
    if (sessionUser)
      dispatch(fetchCartTotal());
  }, [dispatch, sessionUser]);


  return (
    <header className="navigation">
      <div className="nav-left">
        <Link to="/" className="site-logo">
          <img src='https://raw.githubusercontent.com/djdinnebeil/xmas-list-images/refs/heads/main/xmas-list-logo.jpg'
               alt="Site Logo" className="logo"/>
          <span className="site-name">X-Mas List</span>
        </Link>
      </div>
      <div className="nav-right">
        {sessionUser && (
          <>
            <Link to="/create-product" className="add-new-product">Add a New Product</Link>
            <Link to="/favorites" className="get-favorites">
              <PiHeartBold/>
            </Link>
          </>
        )}
        <Link to="/shopping-cart" className="shopping-cart-flex">
          <PiShoppingCartSimple className="shopping-cart-icon"/>
          {sessionUser && totalItems > 0 && <span className="shopping-cart-total">+{totalItems}</span>}
        </Link>
        <ProfileButton className="profile-button-pointer"/>
      </div>
    </header>
  );
}

export default Navigation;
