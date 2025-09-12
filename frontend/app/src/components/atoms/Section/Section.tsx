import type { ReactNode } from "react";

import './sections.css'

interface SectionProps { 
    children:ReactNode;
    width: 'none' | 's' | 'm' | 'l';
    top: 'none' | 's' | 'm' | 'l';
    bottom?: 'none' | 's' | 'm' | 'l';
    left?: 'none' | 's' | 'm' | 'l';
    right?: 'none' | 's' | 'm' | 'l';
    border?: 'none' | 's' | 'm' | 'l';
    position?: 'center';
    padding?:'none' | 's';
    background:'light' | 'primary' | 'alt';
}
export default function Section ({ children, top, background, width, position, padding, border, bottom }: SectionProps) { 
    
    const className = `section top--${top} background--${background} width--${width} position--${position} padding--${padding} border--${border} bottom--${bottom}`
    return (
        <section className={className} >
            {children}
        </section>
    )
}