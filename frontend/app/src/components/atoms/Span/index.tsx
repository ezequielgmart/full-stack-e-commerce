import './spans.css'

import type { SpanProps } from '../../../types';
import { generateClassName } from "../../../utils/components";

export default function Span({ type, variant, size, children }:SpanProps){
    const tag = `${type}`
    const className = generateClassName(tag, variant, size);

    return (
        <>
            <span className={className}>{children}</span>
        </>
    )
}