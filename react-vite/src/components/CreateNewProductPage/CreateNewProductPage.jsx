import { useState } from 'react';
import {useDispatch, useSelector} from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { thunkCreateProduct } from '../../redux/productReducer';
import './CreateNewProductPage.css';

function CreateNewProductPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [category, setCategory] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const [stock, setStock] = useState('');
  const [imageUrls, setImageUrls] = useState(['', '', '', '', '']);
  const [errors, setErrors] = useState({});

  const handleSubmit = async (e) => {
    e.preventDefault();

    const productData = {
      name,
      category,
      description,
      price,
      stock,
      image_url1: imageUrls[0],
      image_url2: imageUrls[1],
      image_url3: imageUrls[2],
      image_url4: imageUrls[3],
      image_url5: imageUrls[4],
    };

    const response = await dispatch(thunkCreateProduct(productData));
    console.log(response);
    if (response.errors) {
      setErrors(response.errors);
    } else {
      navigate(`/product/${response.id}`); // Redirect to the product page on success
    }
  };

  if (!sessionUser) {
    return <p>You must be logged in</p>
  }

  return (
    <div className="create-product-form-div">
      <h2>Create New Product</h2>
      {typeof errors === 'string' ? (
        <p className="error-create-new-product-page">{errors}</p>
      ) : (
        Object.values(errors).map((error, idx) => (
          <p key={idx} className="error-create-new-product-page">{error}</p>
        ))
      )}
      <form onSubmit={handleSubmit} className="create-product-form">
        <label>
          Name
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </label>
        <label>
          Category
          <input
            type="text"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            required
          />
        </label>
        <label>
          Description
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </label>
        <label className="dollar-sign-price">
          <span className="dollar-sign-span">$</span>
          <input
            type="number"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            required
          />
        </label>
        <label>
          Stock
          <input
            type="number"
            value={stock}
            onChange={(e) => setStock(e.target.value)}
            required
          />
        </label>
        {imageUrls.map((url, index) => (
          <label key={index}>
            Image URL {index + 1}{index === 0 && ' (Required)'}
            <input
              type="url"
              value={url}
              onChange={(e) => {
                const newUrls = [...imageUrls];
                newUrls[index] = e.target.value;
                setImageUrls(newUrls);
              }}
              required={index === 0} // Only the first image URL is required
            />
          </label>
        ))}
        <button type="submit" className="create-new-product">Create Product</button>
      </form>
    </div>
  );
}

export default CreateNewProductPage;
