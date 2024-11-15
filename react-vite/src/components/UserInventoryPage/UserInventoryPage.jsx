import  { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchUserInventory } from '../../redux/productReducer';
import EditProductForm from './EditProductForm';
import OpenModalMenuItem from '../Navigation/OpenModalMenuItem';
import './UserInventoryPage.css';
import {useNavigate} from "react-router-dom";

const UserInventoryPage = () => {
  const dispatch = useDispatch();
  const sessionUser = useSelector(state => state.session.user);
  const userInventory = useSelector((state) => state.products.userProducts);
  const navigate = useNavigate();

  useEffect(() => {
    dispatch(fetchUserInventory());
  }, [dispatch]);

  if (!sessionUser) {
    return <p>You must be logged in</p>
  }

  if (!userInventory) return <p>Loading...</p>;

  return (
    <div className="user-inventory-page">
      <h1>Your Inventory</h1>
      <div className="inventory-grid">
        {userInventory.map((product) => (
          <div key={product.id} className="inventory-container">
            <div className="inventory-item">
              <img src={product.preview_image} alt={product.name} className="product-image"/>
              <h2>{product.name}</h2>
              <p>Quantity: {product.stock}</p>
              <p>Price: ${product.price}</p>
              <p>Description: {product.description}</p>
            </div>
            <div className="inventory-edit-div">
              <OpenModalMenuItem
                itemText="Edit"
                modalComponent={
                  <EditProductForm product={product} onClose={() => navigate(0)}/>
                }
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default UserInventoryPage;
