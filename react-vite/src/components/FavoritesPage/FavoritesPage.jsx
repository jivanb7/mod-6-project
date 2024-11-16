import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import "./FavoritesPage.css";
import {Link, useNavigate} from "react-router-dom";

function FavoritesPage() {
  const sessionUser = useSelector((state) => state.session.user);
  const [favorites, setFavorites] = useState([]);
  const navigate = useNavigate();

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

  const handleRemove = (favoriteId) => {
    fetch(`/api/favorites/${favoriteId}`, {
      method: 'DELETE',
    })
    .then(response => {
      if (response.ok) {
        setFavorites((prevFavorites) =>
          prevFavorites.filter(favorite => favorite.id !== favoriteId)
        );
      } else {
        console.error("Failed to remove favorite");
      }
    })
    .catch(error => console.error("Error removing favorite:", error));
  };


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
              <Link to={`/product/${favorite.product_id}`}>
              <img src={favorite.preview_image} alt={favorite.name}/>
                </Link>
              <div className="favorite-item-content">
                <h2>{favorite.name}</h2>
                <p>Category: {favorite.category}</p>
                <p>Description: {favorite.description}</p>
                <p>Price: ${favorite.price.toFixed(2)}</p>
                <p>Stock: {favorite.stock}</p>
                <div className="favorites-buttons">
                  <button
                    className="favorites-view-button"
                    onClick={() => navigate(`/product/${favorite.product_id}`)}
                  >
                    View
                  </button>
                  &nbsp;
                  <button
                    className="remove-button"
                    onClick={() => handleRemove(favorite.id)}
                  >
                    Remove
                  </button>

                </div>

              </div>
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
