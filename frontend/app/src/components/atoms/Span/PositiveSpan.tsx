import Span from './index'
import type { SpanProps } from '../../../types';

export default function PositiveSpan({ children }:SpanProps){

    return (
        <>
            <Span type='span' variant='positive'>
                {children}
            </Span>
        </>
    )
}