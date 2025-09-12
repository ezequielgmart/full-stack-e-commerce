import './table.css';
import type { ReactNode } from "react";

interface TableProps { 
    children:ReactNode
}

export default function Table({children }:TableProps){ 

    return (
        <table className='items-table'>
            {children}
        </table>
    )
}