import { useNavigate } from 'react-router-dom';
//import './ProductsPage.css';

export default function ProductsPage({product}) {
    const navigate = useNavigate();

    const handleTileClick = () => {
        navigate(`/product/${product.id}`)
    }

    const tileRating = product.average_rating ? `${product.average_rating} (${product.review_count})` : 'New';


    return(
        <div className="product-tile" onClick={handleTileClick}>
            {product.previewImage ? (<img src={product.previewImage} alt={product.name} className="product-image" />): (<div className='placeholder-image'>No Image Avaliable</div>)}
            <div className="product-name-row">
                <p>{product.name} </p>
                <p>{tileRating}</p>
            </div>
            <div className="product-creator">{product.username}</div>
            <div className="product-price">{product.price}</div>
            <button className="button-add-cart">Add to Cart</button>
        </div>
    )
}

