import type { ReactNode } from "react";
import './table.css'
interface TableRowProps { 
    className:string; 
    children:ReactNode
}
export default function TableRow ({className ,children}:TableRowProps){

    const newClassName = `table-row table-row--${className}`

    return (

        
        <tr className={newClassName}>

                {children}

        </tr>

    )
}