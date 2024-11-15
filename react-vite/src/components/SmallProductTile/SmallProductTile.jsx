import { useNavigate } from 'react-router-dom';
import { FaPlus } from 'react-icons/fa'; 
import { FaUser } from 'react-icons/fa';
import { FaStar } from 'react-icons/fa';
import './SmallProductTile.css'

export default function ProductsPage({product}) {
    const navigate = useNavigate();

    const handleTileClick = () => {
        navigate(`/product/${product.id}`)
    }

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
    <div className="small-product-price">${product.price}</div>
    <button className="small-button-add-cart"><FaPlus className="small-plus-icon" />                                                                                    Add to Cart</button>
</div>
  );
}