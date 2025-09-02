

import './articles.css';
import type { ProductDetailProps } from '../../../types';

import ProductActionContainer from '../../molecules/Card/ProductActionContainer';

import ImgViewer from '../../molecules/ImgViewer';
import CurrencySpan from '../../atoms/Span/CurrencySpan';
import ItemDetail from '../../molecules/Items/ItemDetail';
import Span from '../../atoms/Span/Span';



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
                    <a href='#'>Deliver to United States</a>
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
                    <ul>
                        <li>NVIDIA GeForce RTX 40 Series: NVIDIA GeForce RTX 4080 Laptop GPU 12GB GDDR6.Adapter : 280W, Battery Li Polymer : 99Wh</li>
                        <li>Intel 13th Gen Ready: i7-13700H Processor 5.0 GHz</li>
                        <li>DDR5 Ready: DDR5 4800 8GB2 (16GB), 1TB Storage (Gen4 M.2 SSD)</li>
                        <li>Cutting-Edge Display: 17.3" Thin Bezel FHD 1920x1080, 360Hz, 100% sRGB, TÜV Rheinland Certified</li>
                        <li>Next Gen Interface: Windows 11 Home AD, Intel Wi-Fi 6E, Bluetooth V5.2</li>
                        <li>Dynamic Audio: Built-in Microphone, 2x 2W Speakers</li>
                        <li>IO: 1x Thunderbolt 4 (Supports Power Delivery), 1x HDMI 2.1, 1x Mini DP 1.4 (120Hz), 2x USB 3.2 Gen1 (Type-A), 1x RJ45, 1x Audio Combo Jack, 1x DC In</li>
                    </ul>
                </div>
            </div>
            <div className="product-detail-article-col">
                <ProductActionContainer data={data}/>
            </div>
        </article>
    );
}

/*

Brand	GIGABYTE
Model Name	AORUS 17 BSF-73US654SH
Screen Size	17.3
Color	Black
Hard Disk Size	1 TB
CPU Model	Core i7
Ram Memory Installed Size	16 GB

*/