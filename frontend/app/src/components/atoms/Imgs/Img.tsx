import './imgs.css'

import { PUBLIC_PRODUCTS_DIR } from '../../../../utils/constants';

import type { CardImgProps } from '../../../types';

export default function IMG({ src,className }:CardImgProps){
    const productImg = PUBLIC_PRODUCTS_DIR + src

    return (
        <>
            <img className={className} src={productImg}/>
        </>
    )
}