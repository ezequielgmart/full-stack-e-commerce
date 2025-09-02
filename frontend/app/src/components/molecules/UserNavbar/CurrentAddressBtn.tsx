
import CurrentAddressIcon from '../../atoms/Button/AddressIcon';
// import Span from '../../atoms/Span/span';
import Strong from '../../atoms/Span/Strong';
import './index.css'

export default function CurrentAddressBtn(){
  return (
    <div className="user-address-navbar-section">
        
        
        {/* <Span className='span-navbar-white-s' value="Deliver to"/> */}
        <CurrentAddressIcon />
        <Strong className='strong-navbar-white-s' value="United States"/>
        

    </div>
  );
};

