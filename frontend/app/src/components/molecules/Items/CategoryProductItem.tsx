
import ItemImg from "../../atoms/Imgs/ItemImg";
import NeutralSpan from "../../atoms/Span/NeutralSpan";

// types
import type { ItemProps } from "../../../types"

import './items.css';


export default function CategoryProductItem({ itemName, ImgSrc }:ItemProps){

    return(
        <div className="item-container">
            <div className="item-container-head">
                <ItemImg src={ImgSrc}/>
            </div>
            <div className="item-container-body">
                <NeutralSpan value={itemName}/>
            </div>
        </div>
    )
}
