import {useEffect, useState} from 'react';
import './OrderHistoryPage.css';
import {useSelector} from "react-redux";

const OrderHistoryPage = () => {
  const sessionUser = useSelector((state) => state.session.user);
  const [orders, setOrders] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchOrders = async () => {
      if (!sessionUser) return;
      try {
        const response = await fetch('/api/orders/current');
        if (response.ok) {
          const data = await response.json();
          setOrders(data.orders || []);
        } else {
          setError("Failed to load orders");
        }
      } catch (error) {
        console.error("Error fetching order history:", error);
        setError("Error fetching order history");
      }
    };
    fetchOrders();
  }, [sessionUser]);

  if (!sessionUser) {
    return <p>You must be logged in</p>
  }

  return (
    <div className="order-history-page">
      <h1>Your Order History</h1>
      {error && <p className="error-message">{error}</p>}
      {orders.length === 0 && !error ? (
        <p className="no-orders">No orders found.</p>
      ) : (
        <div className="order-list">
          {orders.map((order, index) => (
            <div key={order.id || index} className="order-card">
              <h2>Order {index + 1}</h2>
              <p><strong>Date:</strong> {order.created_at ? new Date(order.created_at).toLocaleDateString() : "N/A"}</p>
              <p><strong>Total:</strong> ${order.total ? order.total.toFixed(2) : "N/A"}</p>
              <div className="order-details">
                <h3>Items:</h3>
                {order.details ? (
                  order.details.split("; ").map((item, itemIndex) => (
                    <p key={itemIndex} className="order-item">{item}</p>
                  ))
                ) : (
                  <p className="no-items">No items available</p>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default OrderHistoryPage;