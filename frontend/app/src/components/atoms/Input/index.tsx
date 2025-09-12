import './input.css'

interface InputProps { 
    type: string;
    variant?:string;
    size?:string;
    placeholder?:string;
    customClassName?:string; 
}
export default function Input({type, variant, size, placeholder, customClassName}:InputProps) {

    const className = `${type} ${type}--${variant} ${type}--${size}`

    return (
        
        <input 
            type={type}
            className={customClassName ? customClassName : className}
            placeholder={placeholder}
        />

    );
}