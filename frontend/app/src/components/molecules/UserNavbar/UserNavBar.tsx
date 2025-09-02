
import Span from '../../atoms/Span/Span';
import Strong from '../../atoms/Span/Strong';
import './index.css'

function UserNavBar() {

    return (

            <div className="user-navbar-container">
                    <Span className='span-navbar-white-s' value="Hello, sign in"/><br />
                    <Strong className='strong-navbar-white-s' value="Your account"/>
            </div>


    )
}

export default UserNavBar;
