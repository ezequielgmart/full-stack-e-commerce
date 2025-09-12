import { Link as RouterLink } from 'react-router-dom'; // Importa el Link con un alias
import type { LinkProps } from '../../../types/index.ts'
import { generateClassName } from "../../../utils/components.ts";
import './links.css'

export default function Link({ type, variant, size, href, children }: LinkProps) {
    const className = generateClassName('link', variant, size);

    // Usa RouterLink en lugar de 'a', y la prop es 'to' en lugar de 'href'
    return (
        <RouterLink
            type={type}
            to={href} // <-- La prop correcta es 'to'
            className={className}
        >
            {children}
        </RouterLink>
    );
}