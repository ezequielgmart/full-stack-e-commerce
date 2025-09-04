
import './articles.css';
import type { ProductDetailProps } from '../../../types';

import ProductActionContainer from '../../molecules/Card/ProductActionContainer';

import ImgViewer from '../../molecules/ImgViewer';
import CurrencySpan from '../../molecules/CurrencySpan';
import ItemDetail from '../../molecules/Items/ItemDetail';
import Span from '../../atoms/Span';
import ProductDetailList from '../../molecules/lists/ProductDetailList';


export default function ProductDetailArticle({ data }:ProductDetailProps){

    return (
        <article className="product-detail-article-container">
            <div className="product-detail-article-col">
                <ImgViewer data={data}/>
            </div>
            <div className="product-detail-article-col">
                <div className="product-detail-title">
                    <Span className="product-detail-title-h1" value={data.description}/>
                </div>
                <div className="product-detail-currency">
                    <CurrencySpan amount={data.unit_price}/>
                </div>
                <div className="product-detail-address">
                    <a href='#'><Span className="component-span-s" value="Deliver to United States"/></a>
                </div>
                <div className="product-detail-list">
                    <ItemDetail detail="Brand" value="Gygabyte"/>
                    <ItemDetail detail="Model Name" value="AORUS 17 BSF-73US654SH"/>
                    <ItemDetail detail="Screen size" value="17.3"/>
                    <ItemDetail detail="Color" value="Black"/>
                    <ItemDetail detail="CPU Model" value="Core i7"/>
                    <ItemDetail detail="Ram installed" value="16 GB"/>
                </div>
                <div className="product-detail-about">
                    <h3>About this item:</h3>
                    <ProductDetailList/>
                </div>
            </div>
            <div className="product-detail-article-col">
                <ProductActionContainer data={data}/>
            </div>
        </article>
    );
}

