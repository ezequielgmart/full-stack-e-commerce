import type { ReactNode } from 'react';

export interface ProductData {
  itemName: string;
  ImgSrc: string;

}

export interface FullProductData{
    
  itemName: string;
  description:string;
  unitPrice:number;
  stock:number;
  images:Array<string>;
}

export interface Product { 
    product_id: string;
    name: string;
    description: string;
    unit_price: number;
    stock: number;
    category_name: string;
    images: Array<string>;
}

export interface ProductCover { 
    product_id: string;
    name: string;
    description: string;
    unit_price: number;
    stock: number;
    category_name: string;
    image: string;
}


/* ************* PROPS **********/

export interface BtnProps{
    variant:string; // success / primary / alert
    size:string; // big, medium, small
    onClick: ()=>void; // function 
    children:ReactNode ; // the value the btn shows like Search / etc or the icon
}

export interface ImgProps{
    
    src:string; // /products/laptop 1.jpg
    variant:string; // success / primary / alert
    size:string; // big, medium, small


}

export interface InputProps{
    
    type:string; // text, text-area
    variant:string; // success / primary / alert
    size:string; // big, medium, small
    placeholder:string; // something to show when it's empty

}

export interface LinkProps{ 
    
    href:string; // /products /home
    type:string; // Title, Sub-title,
    variant:string; //  Neutral, alert
    size:string; // big, medium, small
    children:ReactNode ; // the value the atom shows like Search / etc or the icon
    
}

export interface SpanProps{ 
    
    type:string; // Strong, Span
    variant:string; //  Neutral, alert
    size:string; // big, medium, small
    children:ReactNode ; // the value the atom shows like Search / etc or the icon
}

export interface TitleProps{
    level:string; // 1 for h1, 2 for h2, etc
    variant:string; //  Neutral, alert
    size:string; // big, medium, small
    children:ReactNode ; // the value the atom shows like Search / etc or the icon
}

export interface BtnLinkProps {
  /** La URL a la que el enlace debe navegar. */
    href: string;
  
    variant:string; //  Neutral, alert
    size:string; // big, medium, small

    type:string; // search, action
  
    /** El contenido del enlace (texto, ícono, etc.). */
    children: ReactNode;

}
/* molecules  */
export interface NavSectionProps{
    columns:'1' | '2' | '3' | '4';
    header:ReactNode;
    body:ReactNode;
}
/* ************* END OF PROPS **********/