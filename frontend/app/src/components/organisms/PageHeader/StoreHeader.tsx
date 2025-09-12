import type { ReactNode } from "react"
interface HeaderProps { 

    children:ReactNode
}

export default function PageHeader({ children }:HeaderProps){

    return (
        <header>
            { children }
            
        </header>
    );
}
