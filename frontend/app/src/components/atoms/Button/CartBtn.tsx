// import { FaShoppingCart } from "react-icons/fa";
import { FiShoppingCart } from "react-icons/fi";
// import { MdShoppingCart } from "react-icons/md";
import './buttons.css';
// Define la interfaz
interface ShoppingCartProps {
    onClickHandler: () => void;
}

// Aplica la interfaz a las props del componente
// esto ira dentro del div de cada componente del navbar
function ShoppingCart({ onClickHandler }: ShoppingCartProps) {
    return (
        <>
            <div 
            className="shopping-cart-btn"
            onClick={onClickHandler}
            style={{ color: 'white'}}>
            <FiShoppingCart className="nav-bar-icon-m"/>
            </div>
        </>
    );
}

export default ShoppingCart;