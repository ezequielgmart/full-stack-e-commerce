import './spans.css'

import type { TextProps } from '../../../types'

export default function NeutralSpan({ value }:TextProps){
    return (

            <span className="span-neutral">{value}</span>

    )
}