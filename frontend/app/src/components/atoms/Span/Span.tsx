import './spans.css'

import type { GenericSpanProps } from '../../../types';


export default function Span({ value,className }:GenericSpanProps){
    return (
        <>
            <span className={className}>{value}</span>
        </>
    )
}