import type { BtnProps } from "../../../types";
import { generateClassName } from "../../../utils/components";

/* 
* variant: success / primary / alert
* size: big, medium, small
* onClick: function 
* children: the value the btn shows like Search / etc or the icon
*/ 

export default function Button({ variant,  size, children, onClick}: BtnProps) {

    /* generate the class name dinamyc */
    const className = generateClassName('btn', variant, size);

    return (    
        
        <button  
            className={className}
            onClick={onClick} 
        >
            {children}
        </button>

    );
}
