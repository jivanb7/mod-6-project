import { useDispatch } from 'react-redux';
import { thunkDeleteProduct } from '../../redux/productReducer';
import { useModal } from '../../context/Modal';
import './DeleteProductForm.css';

const DeleteProductForm = ({ productId, onClose }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    const handleDelete = async () => {
        await dispatch(thunkDeleteProduct(productId));
        closeModal();
        onClose();
    };

    return (
        <div className="confirm-delete-product-modal">
            <h2>Confirm Delete</h2>
          <br/>
            <p>Are you sure you want to delete this product?</p>
          <br/>
          <div className="delete-product-buttons">
            <button className="red-button-delete-product" onClick={handleDelete}>
                Yes (Delete Product)
            </button>
            <button className="dark-grey-button-cancel-delete-product" onClick={closeModal}>
                No (Keep Product)
            </button>
          </div>
        </div>
    );
};

export default DeleteProductForm;
