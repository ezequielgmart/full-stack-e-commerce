// import React from 'react';

import type { BtnLinkProps  } from '../../../types'; 

import './buttons.css';

/**
 * 
 * **Atom** 
 * ButtonLink: A link that works like a buton. 
 * Used for navigation actions which needs to highligh visually
 *  
*/

export default function ButtonLink({ 
    href, 
    variant, 
    size, 
    type,
    children
}:BtnLinkProps){ 

    // const linkclassName = `link link--${variant} link--${size}`
    const btnClassName = `btn btn--${variant} btn--${size} btn--${type}`

    return (
        <div className={btnClassName}>
            <a
                href={href}
            >
                {children}
            </a>
        </div>

    )
}

