// ShoppingCart.js
import {useEffect, useState} from 'react';
import './ShoppingCart.css';
import {useSelector} from "react-redux";
import { useNavigate } from "react-router-dom";


const ShoppingCart = () => {
  const [cartItems, setCartItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [editingId, setEditingId] = useState(null);
  const [newQuantity, setNewQuantity] = useState({});
  const [purchasedItems, setPurchasedItems] = useState(null);
  const [errorMessage, setErrorMessage] = useState('');

  const sessionUser = useSelector(state => state.session.user);
  const navigate = useNavigate();



  useEffect(() => {
    // Only fetch cart items if a user is logged in
    if (sessionUser) {
      setLoading(true);
      fetch('/api/cart/current')
        .then((response) => response.json())
        .then((data) => {
          setCartItems(data);
          setLoading(false);
        })
        .catch((error) => {
          console.error("Error fetching cart items:", error);
          setLoading(false);
        });
    }
  }, [sessionUser]);

  const handleDelete = (cartItemId) => {
    fetch(`/api/cart/${cartItemId}`, {method: 'DELETE'})
      .then(response => {
        if (response.ok) {
          setCartItems(prevItems => prevItems.filter(item => item.id !== cartItemId));
        } else {
          console.error('Error deleting cart item');
        }
      })
      .catch(error => console.error('Error deleting cart item:', error));
  };

  const handleEditClick = (cartItemId, currentQuantity) => {
    setEditingId(cartItemId);
    setNewQuantity({...newQuantity, [cartItemId]: currentQuantity});
  };

  const handleQuantityChange = (e, cartItemId) => {
    setNewQuantity({...newQuantity, [cartItemId]: e.target.value});
  };

  const handleUpdate = (cartItemId) => {
    const updatedQuantity = newQuantity[cartItemId];
    fetch(`/api/cart/${cartItemId}`, {
      method: 'PUT',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({quantity: updatedQuantity})
    })
      .then(response => {
        if (response.ok) {
          setCartItems(prevItems =>
            prevItems.map(item =>
              item.id === cartItemId ? {...item, quantity: updatedQuantity} : item
            )
          );
          setEditingId(null);
          setErrorMessage('');
        } else {
          return response.json().then(data => {
            const errorMsg = data.error || 'Error updating quantity';
            setErrorMessage(errorMsg);
          });
        }
      })
      .catch(() => {
        setErrorMessage('Error updating quantity');
      });
  };

  const handleCheckout = () => {
    fetch('/api/cart/checkout', {method: 'POST'})
      .then(response => response.json())
      .then(data => {
        setPurchasedItems(data.purchased_items);
        setCartItems([]); // Clear the cart items after checkout
        navigate('/orders'); // Redirect to /orders after checkout

      })
      .catch(error => console.error('Error during checkout:', error));
  };

  if (!sessionUser) {
    return <p>You must log in or sign up to add items to the shopping cart.</p>
  }


  if (loading) {
    return <p>Loading your cart...</p>;
  }

  if (purchasedItems) {
    return (
      <div className="shopping-cart">
        <h2>Thank you for your purchase!</h2>
        <ul className="purchased-items">
          {purchasedItems.map((item, index) => (
            <li key={index}>
              {item.name}: {item.quantity}
            </li>
          ))}
        </ul>
      </div>
    );
  }

  if (!Array.isArray(cartItems) || cartItems.length === 0) {
    return <p>Your cart is empty.</p>;
  }

  return (
    <div className="shopping-cart">
      <h2>Your Shopping Cart</h2>
      <ul className="cart-items">
        {cartItems.map((item) => (
          <li key={item.product_id} className="cart-item">
            <div className="item-details">
              <span className="item-name">{item.name}</span>
              <span className="item-price">${item.price.toFixed(2)}</span>
            </div>

            <div className="item-quantity">
              {editingId === item.id ? (
                <input
                  type="number"
                  min="1"
                  value={newQuantity[item.id] || item.quantity}
                  onChange={(e) => handleQuantityChange(e, item.id)}
                />
              ) : (
                `Quantity: ${item.quantity}`
              )}
            </div>

            <div className="item-total">
              Total: ${(item.total_price).toFixed(2)}
            </div>

            {editingId === item.id ? (
              <button
                className="update-button"
                onClick={() => handleUpdate(item.id)}
              >
                Update
              </button>
            ) : (
              <button
                className="edit-button"
                onClick={() => handleEditClick(item.id, item.quantity)}
              >
                Edit
              </button>
            )}
            <button
              className="delete-button"
              onClick={() => handleDelete(item.id)}
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
      {errorMessage && <p className="error-message">{errorMessage}</p>}

      <button className="checkout-button" onClick={handleCheckout}>
      Checkout
      </button>
    </div>
  );
};

export default ShoppingCart;
