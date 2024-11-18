import {useEffect} from 'react';
import {useDispatch, useSelector} from 'react-redux';
import {fetchUserInventory} from '../../redux/productReducer';
import EditProductForm from './EditProductForm';
import OpenInventoryModalButton from './OpenInventoryModalButton.jsx';
import DeleteProductForm from "./DeleteProductForm.jsx";
import './UserInventoryPage.css';
import {Link, useNavigate} from 'react-router-dom';


const UserInventoryPage = () => {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const userInventory = useSelector((state) => state.products.userProducts);
  const navigate = useNavigate();

  useEffect(() => {
    if (sessionUser) {
      dispatch(fetchUserInventory());
    }
  }, [dispatch, sessionUser]);

  if (!sessionUser) {
    return <p>You must be logged in</p>;
  }

  if (!userInventory) return <p>Loading...</p>;


  return (
    <div className="user-inventory-page">
      <br/>
      <h1>Your Inventory</h1>
      <hr/><br/>
      <div className="inventory-grid">
        {userInventory.length === 0 && <p className="no-items-for-sale">You have no items for sale.</p>}
        {userInventory.map((product) => (
          <div key={product.id} className="inventory-container">
            <Link to={`/product/${product.id}`}>
            <img
              src={product.preview_image}
              alt={product.name}
              className="product-image"
            />
              </Link>
            <div className="inventory-item">
              <h2 className="inventory-item-name">{product.name}</h2>
              <p>Quantity: {product.stock}</p>
              <p>Price: ${product.price}</p>
              <div className="product-description">
                <p>{product.description}</p>
              </div>
              <div className="remove-edit-inventory-div">
                <div className="inventory-edit-div">
                  <OpenInventoryModalButton
                    itemText="Edit"
                    modalComponent={
                      <EditProductForm product={product} onClose={() => navigate(0)}/>
                    }
                  />
                </div>
                <div className="inventory-remove-div">
                  <OpenInventoryModalButton
                    itemText="Remove"
                    modalComponent={
                      <DeleteProductForm productId={product.id} onClose={() => navigate(0)}/>
                    }
                  />
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
      <br/>
      <Link to="/create-product" className="add-new-product-inventory-page">+ Add a New Product</Link>
    </div>
  );
};

export default UserInventoryPage;
