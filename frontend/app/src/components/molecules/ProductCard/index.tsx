import Card from "../Card/Card";

import { Span, Image, Title } from "../../atoms/index";

import type { ProductCardProps } from "../../../types/index";

export default function ProductCard({ 
    product

}:ProductCardProps){ 
 /*
    le voy a pasar data y que tome las cosas que necesita
 */   
    const productTitle = `${product.name} ${product.description}`;


    return (
        <Card
        
            display='grid'
            cols='1'
        >
            <Title
            level="3"
            variant="ligth" 
            size="medium" 
            >{productTitle}</Title>
            {/* <></Span> */}
        </Card>
    )    

}