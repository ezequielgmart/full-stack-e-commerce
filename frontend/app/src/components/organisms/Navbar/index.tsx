
import './navbar.css';
import { Link } from '../../atoms/index.ts';
import { SearchBar, AddressNavSection, ProfileNavSection, OrdersNavSection, CartNavSection } from '../../molecules/index.ts';

export default function NavBar() {

    return (
        <nav className="main-nav-bar">
            <div className="main-nav-bar-container">
                {/* <LogoNavBar/>
                <CurrentAddressBtn/> */}
                <Link
                href='/'
                type='white'
                variant='white'
                size='big'>
                Eshop
                </Link>
                <AddressNavSection/>
                <SearchBar/>
                <ProfileNavSection/>
                <OrdersNavSection/>
                <CartNavSection/>
            </div>
        </nav>
    );
}
