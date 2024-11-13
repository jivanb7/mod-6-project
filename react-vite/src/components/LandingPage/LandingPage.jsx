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
      <div className="header-block" onClick={() => navigate('/product')}>
        <h1>Very Merry Holiday Deals!</h1>
        <button>Shop Now</button>
      </div>

      {/* Category Block */}
      <div className="category-block">
        <h2>Featured Categories</h2>
        <div className="category-list">
          {categories.map(category => (
            <div key={category} className="category-item" onClick={() => navigate(`/product?category=${category}`)}>
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
        <button onClick={() => navigate('/product')}>See All Products</button>
      </div>

      {/* Information Section Block */}
      <div className="info-block">
        <h2>What is Etsy?</h2>
        <h3>Read our wonderfully weird story</h3>
        <div className="info-sections">
          <div className="info-item">
            <h4>A community doing good</h4>
            <p>X-Mas List is a global online marketplace, where people come together to make, sell, buy, and collect unique items. We are also a community pushing for positive change for small businesses, people, and the planet. </p>
          </div>
          <div className="info-item">
            <h4>Support independent creators</h4>
            <p>There is no X-Mas List warehouse, just millions of people selling the things they love. We make the whole process easy, helping you connect directly with makers to find something extraordinary.</p>
          </div>
          <div className="info-item">
            <h4>Peace of Mind</h4>
            <p>Your privacy is the highest priority of our dedicated team. And if you ever need assistance, we are always ready to step in for support.</p>
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
