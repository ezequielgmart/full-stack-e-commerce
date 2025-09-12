import Span from './index'
import type { SpanProps } from '../../../types';

export default function AlertSpan({ children }:SpanProps){

    return (
        <>
            <Span type='span' size='small' variant='outline-alert'>
                {children}
            </Span>
        </>
    )
}