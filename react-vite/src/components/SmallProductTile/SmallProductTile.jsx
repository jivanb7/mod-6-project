import { useNavigate } from 'react-router-dom';
import { useDispatch } from "react-redux";
import { useState } from 'react';
import { addToCart } from "../../redux/cartReducer";
import { FaPlus } from 'react-icons/fa'; 
import { FaUser } from 'react-icons/fa';
import { FaStar } from 'react-icons/fa';
import './SmallProductTile.css'

export default function ProductsPage({product}) {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const [isAddedToCart, setIsAddedToCart] = useState(false);

    const handleTileClick = () => {
        navigate(`/product/${product.id}`)
    }

    const handleAddToCart = (event) => {
        event.stopPropagation();
        if (!isAddedToCart) {
            dispatch(addToCart(product.id));
            setIsAddedToCart(true);
        }
    };

    const tileRating = product.average_rating ? (
        <>
            {product.average_rating} <FaStar className="star-icon" /> ({product.review_count})
        </>
    ) : 'New';

  return (
    <div className="small-product-tile" onClick={handleTileClick}>
    {product.previewImage ? (<img src={product.previewImage} alt={product.name} className="small-product-image" />): (<div className='placeholder-image'>No Image Avaliable</div>)}
    <div className="small-product-name-row">
        <p>{product.name} </p>
        <p>{tileRating}</p>
    </div>
    <div className="small-product-creator"><FaUser className="small-user-icon" />  {product.username}</div>
    <div className="small-product-price">${product.price.toFixed(2)}</div>
    <button 
        className={`button-add-cart ${isAddedToCart ? 'added-to-cart' : ''}`}
         onClick={handleAddToCart}
        disabled={isAddedToCart}
        >
            {isAddedToCart ? 'Added to Cart' : (
                 <>
                    <FaPlus className="plus-icon" /> Add to Cart
                </>
        )}
    </button>
</div>
  );
}