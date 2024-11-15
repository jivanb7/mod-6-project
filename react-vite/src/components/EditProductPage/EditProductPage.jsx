import { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { thunkUpdateProduct } from '../../redux/productReducer';
import {useNavigate} from "react-router-dom";


const EditProductPage = ({ product }) => {
  const dispatch = useDispatch();
  const [name, setName] = useState('');
  const [category, setCategory] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const [stock, setStock] = useState('');
  const [previewImage, setPreviewImage] = useState('');
  const [optionalImages, setOptionalImages] = useState(['', '', '', '']);
  const navigate = useNavigate();

  useEffect(() => {
    if (product) {
      setName(product.name || '');
      setCategory(product.category || '');
      setDescription(product.description || '');
      setPrice(product.price || '');
      setStock(product.stock || '');
      setPreviewImage(product.preview_image || '');
      setOptionalImages([
        product.images?.[1]?.url || '',
        product.images?.[2]?.url || '',
        product.images?.[3]?.url || '',
        product.images?.[4]?.url || '',
      ]);
    }
  }, [product]);

  const handleOptionalImageChange = (index, value) => {
    setOptionalImages((prev) => {
      const newImages = [...prev];
      newImages[index] = value;
      return newImages;
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!product) return; // Ensure product is defined before submitting

    const updatedProduct = {
      id: product.id,
      name,
      category,
      description,
      price,
      stock,
      images: [previewImage, ...optionalImages.filter((img) => img)],
    };
    dispatch(thunkUpdateProduct(updatedProduct));
    navigate('/inventory');
  };

  if (!product) return null; // Return null if product is undefined or null

  return (
    <div className="edit-product-form">
      <h2>Edit Product</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
        </label>

        <label>
          Category:
          <input type="text" value={category} onChange={(e) => setCategory(e.target.value)} />
        </label>

        <label>
          Description:
          <textarea value={description} onChange={(e) => setDescription(e.target.value)} />
        </label>

        <label>
          Price:
          <input type="number" value={price} onChange={(e) => setPrice(e.target.value)} />
        </label>

        <label>
          Stock:
          <input type="number" value={stock} onChange={(e) => setStock(e.target.value)} />
        </label>

        <div className="image-section">
          <h3>Images</h3>
          <label>
            Preview Image (Required):
            <input
              type="url"
              value={previewImage}
              onChange={(e) => setPreviewImage(e.target.value)}
              required
            />
          </label>
          {optionalImages.map((img, index) => (
            <label key={index}>
              Optional Image {index + 1}:
              <input
                type="url"
                value={img}
                onChange={(e) => handleOptionalImageChange(index, e.target.value)}
              />
            </label>
          ))}
        </div>

        <button type="submit" onClick={handleSubmit}>Save Changes</button>
        <button type="button" onClick={navigate('/inventory')}>Cancel</button>
      </form>
    </div>
  );
};

export default EditProductPage;
