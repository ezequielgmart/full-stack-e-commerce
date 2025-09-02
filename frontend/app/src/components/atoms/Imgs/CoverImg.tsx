import './imgs.css'

import type { ItemImgProps } from '../../../types';

export default function ImgCover({ src }:ItemImgProps){
    
    return (
        <>
            <img className="card-cover-img" src={src}/>
        </>
    )
}