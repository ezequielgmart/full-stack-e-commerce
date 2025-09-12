import './titles.css'

import React from 'react'

import type { TitleProps } from '../../../types/index.ts'

export default function Title({ level, variant, size, children, weight}:TitleProps){

    const Tag = `h${level}`
    
    // const className = generateClassName('title', variant, size);
    const className = `title title--${variant} title--${size} title--${weight}`

    return React.createElement(Tag, { className: className }, children);
}