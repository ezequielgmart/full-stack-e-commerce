import type { ReactNode } from "react";
import './asides.css'
interface AsideProps { 
    children:ReactNode;
    classname:string;
}
export default function Aside ({ children, classname }: AsideProps) { 
    
    const className = `aside ${classname}`
    return (
        <aside className={className}>
            {children}
        </aside>
    )
}