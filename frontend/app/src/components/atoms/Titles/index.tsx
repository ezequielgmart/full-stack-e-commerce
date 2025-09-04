import './titles.css'

import React from 'react'

import type { TitleProps } from '../../../types/index.ts'
import { generateClassName } from "../../../utils/components.ts";

export default function Title({ level, variant, size, children}:TitleProps){

    const Tag = `h${level}`
    
    const className = generateClassName('title', variant, size);

    return React.createElement(Tag, { className: className }, children);
}