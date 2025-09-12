import './main.css'

import type { MainProps } from '../../../types';

export default function Main({ 
    className,
    children
}: MainProps){

    return (
        <main className={className}>
            {children}
        </main>
    )
}