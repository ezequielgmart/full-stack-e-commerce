
// import { AddressIcon } from '../../atoms/icons';
// import Span from '../../atoms/Span/span';
import { Link, Span } from '../../atoms/index';

import { useContext } from 'react';
import { AuthContext } from '../../../context/AuthContext.ts';

import NavSection from './index.tsx';

import './index.css'

export default function ProfileNavSection(){

  const auth = useContext(AuthContext);

  return (
    <NavSection
      columns='1'
      header={
        <Span
        type='span'
        variant='darkligth'
        size='small'
        >
          {auth?.user ? `Hello, ${auth?.user.username }` : `Hello, sign in`}
        </Span>
      }
      
      body={

          <Link
          href={auth?.user?.role == 'admin' ? `/admin/dashboard` : `/`}
          type='white'
          variant='white'
          size='medium'>
          {auth?.user?.role == 'admin' ? `Admin Panel` : `Your account`}
          </Link>

      }
    />
  )
}
