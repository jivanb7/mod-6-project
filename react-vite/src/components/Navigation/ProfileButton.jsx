import {useState, useEffect, useRef} from "react";
import {useDispatch, useSelector} from "react-redux";
import {useNavigate} from "react-router-dom";
import {FaUserCircle} from 'react-icons/fa';
import {thunkLogout} from "../../redux/session";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import './ProfileButton.css';


function ProfileButton()
{
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const user = useSelector((store) => store.session.user);
  const ulRef = useRef();
  const navigate = useNavigate();

  const toggleMenu = (e) => {
    e.stopPropagation();
    setShowMenu(!showMenu);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (ulRef.current && !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => setShowMenu(false);

  const logout = (e) => {
    e.preventDefault();
    dispatch(thunkLogout());
    closeMenu();
  };

  const viewOrders = () => {
    closeMenu();
    navigate('/orders');
  };

  const viewInventory = () => {
    closeMenu();
    navigate('/inventory');
  };

  return (
    <>
      <button className="profile-button-pointer" onClick={toggleMenu}>
        <FaUserCircle/>
      </button>
      {showMenu && (
        <ul className={"profile-dropdown"} ref={ulRef}>
          {user ? (
            <>
              <li className="profile-button-no-hover">{user.username}</li>
              <li className="profile-button-no-hover">{user.email}</li>
              <hr/>
              <li>
                <button onClick={viewInventory} className="manage-products-button">Manage Products</button>
              </li>
              <li>
                <button onClick={viewOrders} className="view-orders-button">View Orders</button>
              </li>
              <hr/>
              <li>
                <button onClick={logout} className="logout-button">Log Out</button>
              </li>
            </>
          ) : (
            <>
              <OpenModalMenuItem
                itemText="Log In"
                onItemClick={closeMenu}
                modalComponent={<LoginFormModal/>}
              />
              <OpenModalMenuItem
                itemText="Sign Up"
                onItemClick={closeMenu}
                modalComponent={<SignupFormModal/>}
              />
            </>
          )}
        </ul>
      )}
    </>
  );
}

export default ProfileButton;
