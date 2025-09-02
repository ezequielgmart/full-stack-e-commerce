import './links.css'

import type { TextProps } from '../../../types'

export default function SimpleLink({value}:TextProps){
    return (
        <>
            <a className="a-generic-neutral" href="#">{value}</a>
        </>
    )
}