import './imgs.css'

import type { ItemImgProps } from '../../../types';

export default function ItemImg({ src }:ItemImgProps){
    
    return (
        <>
            <img className="img-items" src={src}/>
        </>
    )
}