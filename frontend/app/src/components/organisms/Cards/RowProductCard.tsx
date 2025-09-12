import { Image, Title, Button, Link, Span } from '../../atoms';

import { CurrencySpan } from '../../molecules';

import './index.css'

interface Product { 
    product_id: string;
    name: string;
    description: string;
    unit_price: number;
    stock: number;
    category_name: string;
    image_url: string;
} 

interface ProductRowProps { 
    data:Product
}

export default function RowProductCard({ data }:ProductRowProps) {

  const className = `card`

  return (
    <Table>


    </Table>
  )
//   return (
//     <article className={className}>
//         <div className="card-header">
//            <div className="card-header-item-container">
            
//                 <div className="card-header-item-container">
//                     <Title level={'3'} size='medium' variant='ligth'>{data.name}</Title>
//                 </div>
                
//                 <div className="card-header-item-container">
//                 <Title level={'4'} size='small' variant='ligth'>{data.description}</Title>
//                 </div>
//                 <div className="card-header-item-container">
//                 <Title level={'4'} size='small' variant='ligth'>{data.product_id}</Title>
//                 </div>
//             </div> 

//             <div className="card-header-info-horizontal">
//                 <div className="card-header-item-container">
//                     <Span type='span' size='medium' variant='primary'>{data.category_name}</Span>
//                 </div>
//                 <div className="card-header-item-container">
//                     <CurrencySpan amount={data.unit_price}></CurrencySpan>
//                 </div> 
                     
//                 <div className={ data.stock > 0 ? "card-header-item-container item--highligh-primary" : "card-header-item-container item--highligh-warning"}>
//                     <Span type='span' size='medium' >{ data.stock > 0 ? data.stock : "Sold out"}</Span>
//                 </div> 
//             </div>
//         </div>
//         <div className="card-body">
//             <div className="card-img-container">
//                 <Image 
//                 src={data?.image_url} 
//                 alt={data.name} 
//                 variant="thumbnail"
//                 />
//             </div>
//             <div className="card-images-carrousel">
//                 <Image 
//                 src={data?.image_url} 
//                 alt={data.name} 
//                 variant="mini-thumbnail"
//                 />
//             </div>
//         </div>
//         <div className="card-footer">
//           <Link href='#' type='hyperlink' variant='neutral' size='small'>See more</Link>
//         </div>
//       {/* <Button>Añadir al carrito</Button> */}
//     </article>
//   )
}