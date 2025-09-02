import type { ProductDetailProps } from '../../../types';
import NoIconBtn from '../../atoms/Button/NoIconBtn';
import CurrencySpan from '../../atoms/Span/CurrencySpan';


export default function ProductActionContainer({ data }:ProductDetailProps){
    const AddCartOnClickHandler = () =>{
        alert("Product added to cart")
    } 
    return (
        <section className="product-actions-card-container">
             <div className="product-actions-header">
                    <CurrencySpan amount={data.unit_price}/>
             </div>
             <div className="product-actions-body">
                <div className="product-actions-body-section">
                    <span>For free shipping <a href='#'>sign in</a></span>
                </div>
                
                <div className="product-actions-body-section">
                    <span>Deliver to <a href='#'>United States</a></span>
                </div>
                <div className="product-actions-body-section">
                    <span>Stock available</span>
                </div>
                <div className="product-actions-body-section">
                    <span>Stock available</span>
                </div>
                <div className="product-actions-body-section">
                    <NoIconBtn className='success-btn' onClick={AddCartOnClickHandler} value="Add to cart"/>
                </div>
                
                <div className="product-actions-body-section">
                    <NoIconBtn className='secondary-btn' onClick={AddCartOnClickHandler} value="Buy now"/>
                </div>
            </div>       
        </section>
    )
}