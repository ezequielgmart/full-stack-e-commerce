// atoms
import SimpleLink from "../../atoms/Link/SimpleLink"
import CardTitle from "../../atoms/Titles/CardTitle"

// molecules
import CategoryProductItem from "../Items/CategoryProductItem"

// types
import type { CategoryProductCardProps } from "../../../types"

// styles
import './cards.css'


export default function CategoryProductCard({categoryTitle, data}:CategoryProductCardProps){

    return(
        <>
            <div className="card-category-product-home-container">
                <div className="card-category-product-home-header">
                    <CardTitle value={categoryTitle}/>
                </div>
                <div className="card-category-product-home-body">
                    {data.map((product, index) => (
                        <CategoryProductItem 
                        key={index} // La "key" es obligatoria en las listas
                        itemName={product.itemName} 
                        ImgSrc={product.ImgSrc} 
                        />
                    ))}
                </div>
                <div className="card-category-product-home-footer">
                    <SimpleLink value="See all deals"/>
                </div>
            </div>
        </>
    )
}