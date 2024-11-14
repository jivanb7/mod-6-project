import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchAllProducts } from "../../redux/productReducer";;
import ProductTile from '../ProductTile';
//import './ProductsPage.css'

export default function ProductsPage() {
    const dispatch = useDispatch();
    const products = useSelector((state) => state.products.products);
  
    useEffect(() => {
      dispatch(fetchAllProducts());
    }, [dispatch]);
  
    return (
      <div className="products-container">
        {products.map((product) => (
          <ProductTile key={product.id} product={product} />
        ))}
      </div>
    );
  }