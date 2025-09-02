import './imgs.css';

import type { ItemImgProps } from '../../../types';

function SliderImg({ src }:ItemImgProps) {
    return (
        <>
            <img className='img-slider' src={src}/>
        </>
    );
}

export default SliderImg;