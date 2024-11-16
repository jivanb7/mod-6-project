import { useModal } from '../../context/Modal';

function OpenInventoryModalButton({
  modalComponent,
  itemText,
  onItemClick,
  onModalClose
}) {
  const { setModalContent, setOnModalClose } = useModal();

  const onClick = (e) => {
    e.preventDefault();
    e.stopPropagation();

    if (onModalClose) setOnModalClose(() => onModalClose);

    setModalContent(modalComponent);
    if (typeof onItemClick === "function") onItemClick();
  };

  return (
    <li className="inventory-button" role="button" tabIndex={0} onClick={onClick} onKeyDown={(e) => e.key === "Enter" && onClick(e)}>
      {itemText}
    </li>
  );
}

export default OpenInventoryModalButton;
