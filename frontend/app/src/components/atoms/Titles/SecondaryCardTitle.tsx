import './titles.css'

import type { TextProps } from '../../../types';

export default function SecondaryCardTitle({value}:TextProps){
    return (
        <>
            <h4 className="card-title">{value}</h4>
        </>
    )
}