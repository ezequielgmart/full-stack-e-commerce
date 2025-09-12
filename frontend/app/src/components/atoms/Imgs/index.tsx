import './imgs.css'

// import { generateClassName } from "../../../utils/components";
import { PUBLIC_PRODUCTS_DIR } from '../../../utils/constants';
import type { ImageProps } from '../../../types';

export default function Image({ src, alt, variant, loading='lazy'}:ImageProps){
    
    const className = `image image--${variant}`
    const imgSrc = `${PUBLIC_PRODUCTS_DIR}${src}`
    return (
        <img
        src={imgSrc}
        alt={alt}
        className={className}
        loading={loading}
        />
    );
}