import './cards.css';

import type { CardTemplateProps } from '../../../types';
/* plantilla reutilizable para hacer cards  sencillas como un product para un carrousel que necesita poca info*/
export default function Card({
    display,
    cols,
    children
}:CardTemplateProps){ 

    const className = `card display--${display} cols--${cols}`

    return (
        <article className={className}>
            {children}
        </article>
    );
}