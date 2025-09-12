import type { ReactNode } from "react";

import './articles.css'

interface ArticleProps { 
    children:ReactNode;
    width?: 'none' | 's' | 'm' | 'l';
    top?: 'none' | 's' | 'm' | 'l';
    left?: 'none' | 's' | 'm' | 'l';
    right?: 'none' | 's' | 'm' | 'l';
    position?: 'center';
    padding?:'none' | 's';
    background?:'light' | 'primary' | 'alt' | 'secondary';
    border?:'none' | 's' | 'm' | 'l';
}
export default function Article ({ children, top, background, width, position, padding, border }: ArticleProps) { 
    
    const className = `article top--${top} background--${background} width--${width} position--${position} padding--${padding} border--${border}`
    return (
        <article className={className} >
            {children}
        </article>
    )
}