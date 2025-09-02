// css
import './cards.css';

// types
import type { ProductCoverCardProps } from '../../../types';

// atoms
import Span from '../../atoms/Span/Span';
import CurrencySpan from '../../atoms/Span/CurrencySpan';
import ProductIMG from '../../atoms/Imgs/ProductImg';


export default function ProductCoverCard({data}:ProductCoverCardProps){


    return(
        <div className='product-cover-card' >
            <div className='product-cover-card-header'>
            <ProductIMG src={data.image} className='img-card-cover'/>
            </div>
            <div className='product-cover-card-body'>
                <div className="product-cover-card-item">
                <a 
                className='link-wrapper'
                href="/product/details">
                    <Span value={data.description} className='product-card-span-highlight'/>
                </a>
                
                </div>
                <div className="product-cover-card-item">
                    <CurrencySpan amount={data.unit_price} className='product-card-span'/>
                </div>
            </div>
        </div>

    )
}