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

export interface ProductListProps { 
    data:Array<ProductCover>;
}

export interface ProductCoverCardProps { 
    data:ProductCover;
}

export interface ProductDetailProps { 
    data:Product;
}

export interface CategoryProductCardProps{
    categoryTitle:string;
    data:Array<ProductData>;

}

export interface ItemDetailprops {
    detail:string;
    value:string;
}

export interface SponsoredProductCardProps{
    data:FullProductData;

}

export interface CardImgProps{
    src:string;
    className:string;
}

export interface ItemImgProps{
    src:string;
}

export interface GenericSpanProps{ 
    
    value:string;
    className:string;
}

export interface CurrencySpanProps{ 
    
    amount:number;

}


export interface GenericTxtProps{ 
    
    value:string;
    className:string;
}


export interface ItemProps{
    itemName:string;
    ImgSrc:string;
}


export interface BtnLinkProps{
    href:string;
    value:string; 
}

// atoms que solo necesiten que se le pase un texto
export interface TextProps{ 
    value:string;
}

export interface BtnProps{
    value:string; 
    onClick: ()=>void;
}
export interface BtnPropsNoClass{
    className:string;
    value:string; 
    onClick: ()=>void;
}
/* ************* END OF PROPS **********/