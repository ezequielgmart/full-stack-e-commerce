// // atoms
// import SimpleLink from "../../atoms/Link/SimpleLink"
// import SecondaryCardTitle from "../../atoms/Titles/SecondaryCardTitle"
// import SecondarySubtitle from "../../atoms/Titles/SecondarySubTitle"
// import NeutralSpan from "../../atoms/Span/NeutralSpan";

// import { PUBLIC_PRODUCTS_DIR } from '../../../utils/constants';

// // types
// import type { SponsoredProductCardProps } from "../../../types"

// // styles
// import './cards.css'
// import ImgCover from "../../atoms/Imgs/CoverImg"


// export default function SponsoredProductCard({data}:SponsoredProductCardProps){
//     const generateImgUrl = (img:string) =>{

//         const imgWith = PUBLIC_PRODUCTS_DIR + img
//         return imgWith
//     }
//     return(
//         <>
//             <div className="sponsored-product-card-container">
//                 <div className="sponsored-product-card-container-header">
                    
//                     <SecondarySubtitle value="Sponsored"/>
//                     <SecondaryCardTitle value="Eshop Recomendations for you"/>
//                 </div>
//                 <div className="sponsored-product-card-container-body">
//                     <div className="card-img-container">
//                         <ImgCover src={generateImgUrl(data.images[3])}/>
//                     </div>
                    
//                     <NeutralSpan value={data.itemName}/>
//                 </div>
//                 <div className="sponsored-product-card-container-footer">
//                     <SimpleLink value="Shop now"/>
//                 </div>
//             </div>
//         </>
//     )
// }