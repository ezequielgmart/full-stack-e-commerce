import type { ReactNode } from "react";
import './table.css'
interface TableColProps { 
    className:'header'; 
    size?:'none' | 'mini' | 's' | 'm' | 'l'; 
    align?:'left' | 'center' | 'right';
    children:ReactNode
}
export default function TableCol ({className ,children, size, align}:TableColProps){
    return (
   
        
        <td className={`table-col table-col--${className} col-size--${size} col-align--${align}`}>
            {children}
        </td>

    )
}