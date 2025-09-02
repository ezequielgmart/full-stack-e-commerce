import './titles.css'

import type { TextProps } from '../../../types';

export default function CardTitle({value}:TextProps){
    return (
        <>
            <h3 className="card-title">{value}</h3>
        </>
    )
}