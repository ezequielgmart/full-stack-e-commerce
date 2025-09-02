
import type { PropsWithChildren } from "react";

import type { TextProps } from "../../../types";

import './links.css'

// Wrapper: its function is wrapp other components therefore there's no need for style or class names here 

export default function LinkWrapper({value}:TextProps, {children}:PropsWithChildren){

    return (
    <a 
    className="link-wrapper"
    href={value}>
        {children}
    </a>
    )

} 