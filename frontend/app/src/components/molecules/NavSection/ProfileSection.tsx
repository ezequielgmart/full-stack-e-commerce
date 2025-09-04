
// import { AddressIcon } from '../../atoms/icons';
// import Span from '../../atoms/Span/span';
import { Link, Span } from '../../atoms/index';

import NavSection from './index.tsx';

import './index.css'

export default function ProfileNavSection(){
  const sectionTitle = 'Hello, sign in'
  const address = 'Your Account'

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
