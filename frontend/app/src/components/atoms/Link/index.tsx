import './links.css'

import type { LinkProps } from '../../../types/index.ts'
import { generateClassName } from "../../../utils/components.ts";

export default function Link({type, variant, size, href, children}:LinkProps) {
    
    const className = generateClassName('link', variant, size);

    return (

        <a 
            type={type}
            className={className}
            href={href}
        >
            {children}
        </a>

    );
}