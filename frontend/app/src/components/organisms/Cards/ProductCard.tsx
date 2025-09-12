import { Image, Title, Button, Link } from '../../atoms';

import { CurrencySpan } from '../../molecules';

import './index.css'

export default function ProductCard({ product }) {
  const className = `card`
  const fullName = `${product.name} ${product.description}`
  return (
    <article className={className}>
        <Image 
          src={product.image_url} 
          alt={product.name} 
          variant="thumbnail"
        />
        <div className="card-body">
          <Title level={'3'} size='small' variant='ligth'>{fullName}</Title>
          <CurrencySpan amount={product.unit_price}></CurrencySpan>
          
        </div>
        {/* <div className="card-footer">
          <Link href='#' type='hyperlink' variant='neutral' size='small'>See details</Link>
        </div> */}
      {/* <Button>Añadir al carrito</Button> */}
    </article>
  )
}