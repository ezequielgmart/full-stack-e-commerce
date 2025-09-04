// import type { ProductDetailProps } from '../../../types';
// import IMG from '../../atoms/Imgs';

// import './img.viewer.css'

// export default function ImgViewer({ data }:ProductDetailProps){

//     let selectedImgForShowing = data.images[0]

//     return (
//         <section className='img-viewer-container'>
//             <div className="img-viewer-body">
//                 <div className="img-viewer-preview-list">
//                     {
//                         data.images.map((element, index)=>(
//                             <IMG src={element} className='img-viewer-preview-item'/> 
//                         ))
//                     }

//                 </div>
//                 <div className='img-viewer-showing-item'>
//                     <IMG src={selectedImgForShowing} className='img-viewer-showing-item'/> 
//                 </div>
//             </div>
//             <div className="img-viewer-footer">
//                     <div className="img-viewer-footer-content">
//                         <a href="#">Click for full view</a>
//                     </div>
//             </div>        
//         </section>
//     )

// }