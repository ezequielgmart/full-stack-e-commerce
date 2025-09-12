import type { ReactNode } from 'react';

/* this represents the Product object that I received from the backend */
export interface Product { 
    product_id: string;
    name: string; 
    description: string; 
    unit_price: number; 
    stock: number | null; 
    category_name:string;
    image_url:string;
}

export interface ProductsApiResponse {
  info: {
    total_items: number;
    total_pages: number;
    per_page: number;
  };
  data: Product[];
}

/* ******** Props for componentes that require a lsit of products *********  */
export interface ListOfProductsProps{
    data:Product[] | null
} 

export interface ProductCardProps {
    product: Product;
}
/* ************* ATOMS PROPS **********/

export interface BtnProps{
    variant?:string; // success / primary / alert
    size?:string; // big, medium, small
    onClick: ()=>void; // function 
    children?:ReactNode ; // the value the btn shows like Search / etc or the icon
    customClassName?:string;
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
export interface ImgProps{
    
    src:string; // /products/laptop 1.jpg
    variant:string; // success / primary / alert
    size:string; // big, medium, small


}

export interface InputProps{
    
    type:string; // text, text-area
    variant?:string; // success / primary / alert
    size?:string; // big, medium, small
    placeholder?:string; // something to show when it's empty

}

export interface LinkProps{ 
    
    href:string; // /products /home
    type:string; // Title, Sub-title,
    variant:string; //  Neutral, alert
    size:string; // big, medium, small
    children:ReactNode ; // the value the atom shows like Search / etc or the icon
    
}

export interface SpanProps{ 
    
    type?:'strong' | 'span'; // Strong, Span
    variant?:string; //  Neutral, alert
    size?:'big' | 'medium' | 'small'; // big, medium, small
    children?:ReactNode ; // the value the atom shows like Search / etc or the icon
}

export interface TitleProps{
    level:'1' | '2' | '3' | '4'; 
    variant: 'neutral' | 'alert' | 'ligth' ; 
    size:'big' | 'medium' | 'small'; 
    weight?:'bold' | 'medium' | 'small'
    children:ReactNode ; // the value the atom shows like Search / etc or the icon
}


export interface ImageProps {
  /** La URL de la fuente de la imagen. */
  src: string;
  
  /** El texto alternativo y descriptivo de la imagen. Es OBLIGATORIO por accesibilidad. */
  alt: string;
  
  /** La variante visual de la imagen (avatar, thumbnail, etc.). */
  variant?: 'thumbnail' | 'avatar' | 'cover' | 'mini-thumbnail';
  
  /** Estrategia de carga. 'lazy' es ideal para imágenes que no están en la parte superior de la página. */
  loading?: 'lazy' | 'eager';
  
}

/* MOLECULES PROPS  */
export interface MainProps{ 
    className:string;
    children:ReactNode

}

export interface NavSectionProps{
    columns:'1' | '2' | '3' | '4';
    header:ReactNode;
    body:ReactNode;
}

export interface CardTemplateProps{ 

    display: 'none' | 'grid';
    cols:'1' | '2' | '3' | '4';

    children:ReactNode

}
/* ************* END OF PROPS **********/