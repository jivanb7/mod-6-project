import { useNavigate } from 'react-router-dom';
import { FaPlus } from 'react-icons/fa'; 
import { FaUser } from 'react-icons/fa';
import { FaStar } from 'react-icons/fa';
import './ProductTile.css'

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
    


    return(
        <div className="product-tile" onClick={handleTileClick}>
            {product.previewImage ? (<img src={product.previewImage} alt={product.name} className="product-image" />): (<div className='placeholder-image'>No Image Avaliable</div>)}
            <div className="product-name-row">
                <p>{product.name} </p>
                <p>{tileRating}</p>
            </div>
            <div className="product-creator"><FaUser className="user-icon" />  {product.username}</div>
            <div className="product-price">${product.price.toFixed(2)}</div>
            <button className="button-add-cart"><FaPlus className="plus-icon" />                                                                                    Add to Cart</button>
        </div>
    )
}

