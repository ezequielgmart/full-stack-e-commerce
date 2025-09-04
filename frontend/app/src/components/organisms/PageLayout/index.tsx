import type { ReactNode } from 'react';
import './page.layout.css';

interface MainProps{ 
    children:ReactNode
}
export default function Main({ children }: MainProps){
    const className = `main margin--m width--8 position--center display--grid cols--2`
    return (
        <main className={className}>
            {children}
        </main>
    )
}