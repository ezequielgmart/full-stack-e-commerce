

import type { ReactNode } from 'react';
import './lists.css';

interface ListProps{ 
    children:ReactNode;
}
export default function AdminAside ({ children }:ListProps) { 
    return (
            <ul className='list list--lateral list--options'>
                {children}
            </ul>

    )
}