import './titles.css'

import type { TextProps } from '../../../types';

export default function SecondarySubtitle({value}:TextProps){
    return (
        <>
            <span className="card-sub-title-secondary">{value}</span>
        </>
    )
}