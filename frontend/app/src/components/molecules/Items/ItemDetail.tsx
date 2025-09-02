import type { ItemDetailprops } from "../../../types"
import './items.css';

export default function ItemDetail ({ detail, value }:ItemDetailprops){
    return (
        
        <div className="detail-item-row">
            <div className="detail-item"><strong className="detail-item-strong">{detail}</strong></div>
            <div className="detail-item"><span className="detail-item-span">{value}</span></div>
        </div>

    )

}