import { Link as RouterLink } from 'react-router-dom'; // Importa el Link con un alias

import './links.css'
import type { ReactNode } from 'react';


export interface LinkProps{ 
    
    href:string; // /products /home
    type?:string; // Title, Sub-title,
    variant?:string; //  Neutral, alert
    size?:string; // big, medium, small
    children?:ReactNode ; // the value the atom shows like Search / etc or the icon
    customClassName?:string; 
    
}

export default function Link({ type, variant, size, href, children, customClassName }: LinkProps) {
    const className = `link link--${variant} link--${size}`
    return (
        <RouterLink
            type={type}
            to={href}
            className={customClassName ? customClassName : className}
        >
            {children}
        </RouterLink>
    );
}