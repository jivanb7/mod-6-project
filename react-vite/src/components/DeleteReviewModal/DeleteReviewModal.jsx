import { useDispatch } from 'react-redux';
import { deleteProductReview } from '../../redux/reviewReducer'; 
import { useModal } from '../../context/Modal';

const DeleteReviewModal = ({ reviewId }) => {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    const handleDelete = async () => {
        await dispatch(deleteProductReview(reviewId));
        closeModal();
    };

    return (
        <div className="confirm-delete-modal">
            <h2>Confirm Delete</h2>
            <p>Are you sure you want to delete this review?</p>
            <button className="red-button" onClick={handleDelete}>
                Yes (Delete Review)
            </button>
            <button className="dark-grey-button" onClick={closeModal}>
                No (Keep Review)
            </button>
        </div>
    );
};

export default DeleteReviewModal;
