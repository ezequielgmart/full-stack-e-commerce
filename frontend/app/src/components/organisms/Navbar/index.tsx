// NOTE: 
// archivo index.tsx
// que lo exporta, haciendo las importaciones más limpias.
import './navbar.css';
import SearchBar from "../../molecules/SearchBar/index.tsx";
import LogoNavBar from "../../molecules/Logo/index.tsx";
import UserNavBar from "../../molecules/UserNavbar/UserNavBar.tsx";
import OrdersNavBar from '../../molecules/UserNavbar/OrdersNavBar.tsx';
import CurrentAddressBtn from '../../molecules/UserNavbar/CurrentAddressBtn.tsx';
import ShoppingCart from '../../atoms/Button/CartBtn.tsx';



function NavBar() {
    const CartOnClickHandler = () =>{
        alert('Click on car')
    }
    return (
        <nav className="main-nav-bar">
            <div className="main-nav-bar-container">
                <LogoNavBar/>
                <CurrentAddressBtn/>
                <SearchBar/>
                <UserNavBar/>
                <OrdersNavBar/>
                <ShoppingCart onClickHandler={CartOnClickHandler}/>
            </div>
        </nav>
    );
}

export default NavBar;