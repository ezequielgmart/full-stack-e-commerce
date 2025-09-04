import './imgs.css'

import { PUBLIC_PRODUCTS_DIR } from '../../../utils/constants';
import { generateClassName } from "../../../utils/components";

import type { ImgProps } from '../../../types';

export default function Image({ src, size, variant }:ImgProps){

    const productImg = `${PUBLIC_PRODUCTS_DIR}/${src}`
    
    const className = generateClassName('img', variant, size);

    return (
        <>
            <img className={className} src={productImg}/>
        </>
    )
}