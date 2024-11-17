import {Link, useNavigate} from 'react-router-dom';
import {useDispatch, useSelector} from "react-redux";
import {useEffect, useState} from 'react';
import {addToCart} from "../../redux/cartReducer";
import {FaHeart, FaPlus, FaRegHeart} from 'react-icons/fa';
import {FaUser} from 'react-icons/fa';
import {FaStar} from 'react-icons/fa';
import './SmallProductTile.css'
import {addToFavorites, fetchFavorites, removeFromFavorites} from "../../redux/favoriteReducer.js";

export default function ProductsPage({product}) {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const currentUser = useSelector((state) => state.session.user);
  const favorites = useSelector((state) => state.favorites.favorites);

  const [isAddedToCart, setIsAddedToCart] = useState(false);

  const [localIsFavorited, setLocalIsFavorited] = useState(false);

  const isOwner = currentUser && currentUser.id === product?.user_id;

  const product_id = product.id;

  const handleTileClick = () => {
    navigate(`/product/${product.id}`)
  }

  useEffect(() => {
    if (currentUser) {
      dispatch(fetchFavorites());
    }
  }, [dispatch, currentUser]);

  useEffect(() => {
    if (favorites && product_id) {
      const isFavorited = favorites.some((favorite) => favorite.product_id === Number(product_id));
      setLocalIsFavorited(isFavorited);
    }
  }, [favorites, product_id]);

  const handleAddToCart = (event) => {
    event.stopPropagation();
    if (!isAddedToCart) {
      dispatch(addToCart(product.id));
      setIsAddedToCart(true);
    }
  };

  const handleFavoriteToggle = async (e) => {
    e.preventDefault();
    e.stopPropagation();
    const optimisticState = !localIsFavorited;
    setLocalIsFavorited(optimisticState);

    try {
      if (optimisticState) {
        await dispatch(addToFavorites(product_id));
      } else {
        await dispatch(removeFromFavorites(product_id));
      }
      await dispatch(fetchFavorites());

    } catch (error) {
      console.error("Error updating favorites:", error);
      setLocalIsFavorited(!optimisticState);
    }
  };

  const tileRating = product.average_rating ? (
    <>
      {product.average_rating} <FaStar className="star-icon"/> ({product.review_count})
    </>
  ) : 'New';

  return (
    <div className="small-product-tile" onClick={handleTileClick}>
      {product.previewImage ? (<img src={product.previewImage} alt={product.name} className="small-product-image"/>) : (
        <div className='placeholder-image'>No Image Avaliable</div>)}
      <div className="small-product-name-row">
        <p>{product.name} </p>
        <p>{tileRating}</p>
      </div>
      <div className="small-product-name-row">
        <div className="small-product-creator"><FaUser className="small-user-icon"/> {product.username}</div>

        {!isOwner && currentUser &&
          <button
            className="favorite-button"
            onClick={handleFavoriteToggle}
          >

            {localIsFavorited ? (
              <FaHeart className="favorite-icon" style={{color: "red"}}/>
            ) : (
              <FaRegHeart className="favorite-icon" style={{color: "gray"}}/>
            )}
          </button>
        }
      </div>
      <div className="small-product-price">${product.price.toFixed(2)}</div>
      {product.stock === 0 && <p>Out of stock</p>}
      {product.stock > 0 && currentUser && !isOwner &&
        <button
          className={`button-add-cart ${isAddedToCart ? 'added-to-cart' : ''}`}
          onClick={handleAddToCart}
          disabled={isAddedToCart}
        >
          {isAddedToCart ? 'Added to Cart' : (
            <>
              <FaPlus className="plus-icon"/> Add to Cart
            </>
          )}
        </button>
      }


      {isOwner && (
        <div className="owner-of-product">
          <p>You own this product</p>
          <Link to="/inventory" onClick={(event) => {
            event.preventDefault();
            event.stopPropagation();
            navigate('/inventory');
          }}>
            <button className="manage-user-inventory">
              Manage your inventory
            </button>
          </Link>
        </div>)
      }
    </div>
  );
}