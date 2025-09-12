import Span from './index'
import type { SpanProps } from '../../../types';

export default function ErrorSpan({ children }:SpanProps){

    return (
        <>
            <Span type='span' variant='error'>
                {children}
            </Span>
        </>
    )
}