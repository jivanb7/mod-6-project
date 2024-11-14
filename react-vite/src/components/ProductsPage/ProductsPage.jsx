import { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchAllProducts } from "../../redux/productReducer";
import ProductTile from '../ProductTile';
import './ProductsPage.css'

export default function ProductsPage() {
    const dispatch = useDispatch();
    const products = useSelector((state) => state.products.products);
  
    const categories = ["All Products", "Ornaments", "Apparel", "Decor", "Gifts", "Baking"]; 

    const [selectedCategory, setSelectedCategory] = useState("All Products");

    useEffect(() => {
        dispatch(fetchAllProducts());
    }, [dispatch]);


    const filteredProducts = selectedCategory === "All Products" ? products
    : products.filter(product => product.category === selectedCategory);
  
    return (
        <div className="main-container">
            <div className="category-bar">
            <span>Category: </span>
            {categories.map((category) => (
                <button
                    key={category}
                    className={`category-button ${category === selectedCategory ? 'selected' : ''}`}
                    onClick={() => setSelectedCategory(category)}
                >
                    {category}
                </button>
            ))}
            </div>
            <div className="products-container">
                {filteredProducts.map((product) => (
                    <ProductTile key={product.id} product={product} />
                ))}
            </div>
      </div>
    );
  }