import type { BtnProps } from "../../../types";

import './buttons.css'
/* 
* variant: success / primary / alert
* size: big, medium, small
* onClick: function 
* children: the value the btn shows like Search / etc or the icon
*/ 

export default function Button({ variant,  size, children, onClick, customClassName}: BtnProps) {

    /* generate the class name dinamyc */
    // const className = generateClassName('btn', variant, size);
    const className = `btn btn--${variant} btn--${size}`

    return (    
        
        <button  
            className={customClassName ? customClassName : className}
            onClick={onClick} 
        >
            {children}
        </button>

    );
}
