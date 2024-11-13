import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import "./FavoritesPage.css";

function FavoritesPage() {
  const navigate = useNavigate();
  const sessionUser = useSelector((state) => state.session.user);
  const [favorites, setFavorites] = useState([]);
  const [errors, setErrors] = useState({});

  useEffect(() => {
    if (sessionUser) {
      fetch('/api/favorites/current')
        .then(response => response.json())
        .then(data => {
          setFavorites(data);
        })
        .catch(error => console.error("Error fetching favorites:", error));
    }
  }, [sessionUser]);

  if (!sessionUser) {
    return <p>You must be logged in</p>
  }
  return (
    <>
      <h1>Your Favorites</h1>
      {favorites.length > 0 ? (
        <ul className="favorites-list">
          {favorites.map((favorite) => (
            <li key={favorite.id} className="favorite-item">
              <h2>{favorite.name}</h2>
              <p>Category: {favorite.category}</p>
              <p>Description: {favorite.description}</p>
              <p>Price: ${favorite.price.toFixed(2)}</p>
              <p>Stock: {favorite.stock}</p>
              <p>Added to Favorites At: {new Date(favorite.created_at).toLocaleString()}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>No favorites found.</p>
      )}
    </>
  );
}

export default FavoritesPage;
