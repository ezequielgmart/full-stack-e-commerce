import type { ReactNode } from "react";
import './lists.css'
interface ListContainerProps { 
    children:ReactNode
}

export default function ListContainer ({ children }: ListContainerProps){ 

    return (
        <article className='list-container'>
            { children }
        </article>
    )
}