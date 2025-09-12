import Span from './index'
import type { SpanProps } from '../../../types';

export default function SpanTable({ children }:SpanProps){

    return (
        <>
            <Span type='span' size='small' variant='darkligth'>
                {children}
            </Span>
        </>
    )
}