
// import { AddressIcon } from '../../atoms/icons';
// import Span from '../../atoms/Span/span';
import { Link, Span } from '../../atoms/index';

import NavSection from './index.tsx';

import './index.css'

export default function OrdersNavSection(){
  const sectionTitle = 'History'
  const address = 'Your Orders'

  return (
    <NavSection
      columns='1'
      header={
        <Span
        type='span'
        variant='darkligth'
        size='small'
        >
          {sectionTitle}
        </Span>
      }
      
      body={

          <Link
          href='/product/details'
          type='link'
          variant='white'
          size='medium'>
          {address}
          </Link>

      }
    />
  )
}
