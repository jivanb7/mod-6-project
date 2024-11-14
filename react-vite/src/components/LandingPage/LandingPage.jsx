import { useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux'
import SmallProductTile from '../SmallProductTile';
import './LandingPage.css';

export default function LandingPage() {
  const navigate = useNavigate();

  const products = useSelector(state => state.products.products);
  const featuredProducts = products.slice(0, 5);


  return (
    <div className="landing-page">
      {/* Header Block */}
      <div className="header-block">
        <div className="header-content">
          <h1 className="kalnia-title">Very merry deals!</h1>
          <p className="subtitle">Celebrate the holidays with handcrafted gifts</p>
          <button onClick={() => navigate('/product')} className="shop-button">Shop deals</button>
        </div>
        <div className="header-image">
          <img src="https://i.imgur.com/J00IwtY.png" alt="Family Christmas" />
        </div>
      </div>

      {/* General Block */}
      <div className="general-block">
      <h2>Amazing deals, updated daily</h2>
      <div className="product-list">
        {featuredProducts.map(product => (
          <SmallProductTile key={product.id} product={product} />
        ))}
      </div>
      <button onClick={() => navigate('/product')} className="shop-button">See All Products</button>
    </div>

      {/* Information Section Block */}
      <div className="info-block">
        <h2>What is X-Mas List?</h2>
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
          <div className="help-text">Have a question? Well, we got some answers</div>
          <button onClick={() => window.open("https://www.youtube.com/watch?v=CxAcgbKUFb4", "_blank")} className="shop-button">
            Go to Help Center
          </button>
        </div>
      </div>
    </div>
  );
}
