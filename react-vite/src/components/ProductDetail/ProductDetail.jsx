import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { fetchProductDetail } from "../../redux/productReducer";

function ProductDetail() {
  const dispatch = useDispatch();
  const { product_id } = useParams();

  const product = useSelector((state) => state.products.product);
  const error = useSelector((state) => state.products.error);

  useEffect(() => {
    dispatch(fetchProductDetail(product_id));
  }, [dispatch, product_id]);

  if (error) {
    return <div>{error}</div>;
  }

  if (!product) {
    return;
  }

  return (
    <div>
      <div className="product-detail">
        <h1>{product.name}</h1>
        {product.preview_image && (
          <img
            src={product.preview_image.image_url}
            alt={product.name}
          />
        )}
        <p>{product.description}</p>
        <p>Price: ${product.price}</p>
        <p>Stock: {product.stock} available</p>
      </div>

      <div>
        <h1>REVIEWS</h1>
      </div>
    </div>
  );
}

export default ProductDetail;
