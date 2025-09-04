
import { ShoppingCart } from '../../atoms/icons.tsx';
// import Span from '../../atoms/Span/span';
import { Link, Span } from '../../atoms/index';

import './index.css'

export default function CartNavSection(){
  const itemsQty = '9+';

  return (

        <div className='navbar-btn navbar-btn--super-padding'>
          <div className='cart-body-container'>
            <Link
            href='/product/details'
            type='icon'
            variant='white'
            size='big'>
            <Span
            type='span'
            variant='ligth'
            size='x-big'
            >
              <ShoppingCart />
            </Span>
            </Link>
          </div>
          <div className='cart-baloon-items-qty'>

            <Span
            type='span'
            variant='ligth'
            size='small'
            >
              {itemsQty}
            </Span>
          </div>
        </div>

  )
}
