import './input.css'

import type { InputProps } from '../../../types/index.ts'

export default function Input({type, variant, size, placeholder}:InputProps) {
    
    const className = `${type} ${type}--${variant} ${type}--${size}`

    return (
        
        <input 
            type={type}
            className={className}
            placeholder={placeholder}
        />

    );
}