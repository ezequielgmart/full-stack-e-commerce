
import { AddressIcon } from '../../atoms/icons';
// import Span from '../../atoms/Span/span';
import { Link, Span } from '../../atoms/index';

import NavSection from './index.tsx';

import './index.css'

export default function AddressNavSection(){
  const sectionTitle = 'Delivering to'
  const address = 'Update Location'

  return (
    <NavSection
      columns='2'
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
        <>
          <Span
          type='span'
          variant='ligth'
          size='big'
          >
          <AddressIcon />
          </Span>
          <Link
          href='/product/details'
          type='link'
          variant='white'
          size='medium'>
          {address}
          </Link>
        </>
      }
    />
  )
}
