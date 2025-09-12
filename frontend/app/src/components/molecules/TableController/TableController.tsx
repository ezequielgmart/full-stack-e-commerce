import type { ReactNode } from "react";
import { Span } from "../../atoms"
import { ArrowDownIcon } from "../../atoms/icons"

interface TableControllerProps { 

    children:ReactNode;
    customClassName?:string; 

}
export default function TableController ({ children }:TableControllerProps){ 
    
    return (
        <div className='container'>
            <Span type="strong" size="small" variant='darkligth'>
                {children}
            </Span>
            <Span type="strong" size="small" variant='darkligth'>
                <ArrowDownIcon/>
            </Span>
        </div>
    )
}