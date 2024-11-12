import { useNavigate } from 'react-router-dom';
import './LandingPage.css';

export default function LandingPage() {
  const navigate = useNavigate();

  // Placeholder product data until the API is ready
  const categories = ["Ornaments", "Apparel", "Decor", "Gifts", "Baking"];
  const products = [
    { id: 1, title: "Sample Product 1", price: "$28.28", rating: 4.9, reviews: 690 },
    { id: 2, title: "Sample Product 2", price: "$35.00", rating: 4.8, reviews: 500 },
    
  ];

  return (
    <div className="landing-page">
      {/* Header Block */}
      <div className="header-block" onClick={() => navigate('/products')}>
        <h1>Very Merry Holiday Deals!</h1>
        <button>Shop Now</button>
      </div>

      {/* Category Block */}
      <div className="category-block">
        <h2>Featured Categories</h2>
        <div className="category-list">
          {categories.map(category => (
            <div key={category} className="category-item" onClick={() => navigate(`/products?category=${category}`)}>
              {category}
            </div>
          ))}
        </div>
      </div>

      {/* General Block */}
      <div className="general-block">
        <h2>Amazing deals, updated daily</h2>
        <div className="product-list">
          {products.map(product => (
            <div key={product.id} className="product-item">
              <div className="product-image">[Image]</div>
              <div className="product-info">
                <p className="product-title">{product.title}</p>
                <p className="product-price">{product.price}</p>
                <p className="product-rating">{product.rating} ({product.reviews})</p>
              </div>
            </div>
          ))}
        </div>
        <button onClick={() => navigate('/products')}>See All Products</button>
      </div>

      {/* Information Section Block */}
      <div className="info-block">
        <h2>What is Etsy?</h2>
        <h3>Read our wonderfully weird story</h3>
        <div className="info-sections">
          <div className="info-item">
            <h4>A community doing good</h4>
            <p>Description about community initiatives on Etsy.</p>
          </div>
          <div className="info-item">
            <h4>Support independent creators</h4>
            <p>Description about Etsy supporting creators.</p>
          </div>
          <div className="info-item">
            <h4>Peace of Mind</h4>
            <p>Description about customer security and trust on Etsy.</p>
          </div>
        </div>
        <div className="help-center">
          <p>Have a question? Well, we got some answers</p>
          <button onClick={() => window.open("https://www.youtube.com/watch?v=CxAcgbKUFb4", "_blank")}>
            Go to Help Center
          </button>
        </div>
      </div>
    </div>
  );
}
