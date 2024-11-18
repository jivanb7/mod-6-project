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
        <div style={{width: "325px"}} className="confirm-delete-modal">
            <h2>Confirm Delete</h2>
            <p style={{textAlign: "center"}}>Are you sure you want to delete this review?</p>
            <div style={{width: "315px", display: "flex", justifyContent: 'space-evenly', height: "43px", marginTop: "5px"}}>
            <button style={{color: "white", backgroundColor: "red", height: "30px", borderRadius: "10px"}} className="red-button" onClick={handleDelete}>
                Yes (Delete Review)
            </button>
            <button style={{color: "white", backgroundColor: "black", height: "30px", borderRadius: "10px"}} className="dark-grey-button" onClick={closeModal}>
                No (Keep Review)
            </button>
            </div>
        </div>
    );
};

export default DeleteReviewModal;
