import { Link } from 'react-router-dom';
import type { Product } from '../../../types/index'
import { TableRow, TableCol, Image, PositiveSpan, Span, ErrorSpan, SpanTable } from '../../atoms';

import './table.molecules.css'
interface TableProductRowProps { 
    number?:number; // number on the 
    data:Product;
}
export default function TableProductRow ({ number, data }:TableProductRowProps){    
    const getProductStatus = (stock: number | null): string => {
    const currentStock = stock ?? 0;

        if (currentStock > 10) {
            return "In stock";
        }  else { // Esto solo captura 0 y negativos
            return "Sold out";
        }
    };
    
    const currencyFormat = new Intl.NumberFormat('es-DO', {
        style: 'decimal',
        minimumFractionDigits: 2,  // Siempre muestra 2 decimales
        maximumFractionDigits: 2,
    });
    
    const status = getProductStatus(data.stock);

    return (                        
        <TableRow className='item-row' key={data.product_id} >
            <TableCol className='col' size='s' align='center'>
                <Image src={data.image_url} alt='' variant='mini-thumbnail' loading='lazy'/>
            </TableCol>
            <TableCol className='col' size='l' align='left'>
                <a href={data.product_id}>
                    <SpanTable>{`${data.name} ${data.description}`}</SpanTable>
                    
                </a>
            </TableCol>
            <TableCol className='col' size='m'>
                
                <SpanTable>
                    {data.category_name}
                </SpanTable>

            </TableCol>
            <TableCol className='col' size='mini' align='right'>
                
                <SpanTable>
                    ${currencyFormat.format(data.unit_price)}
                </SpanTable>

            </TableCol>
            <TableCol className='col' size='m' align='center'>
                {/* Ahora la lógica es más limpia. Si el status es "Available", usa PositiveSpan.
                Para cualquier otro status, usa Span. */}
                {status === "In stock" ? (
                    <PositiveSpan>{status}</PositiveSpan>
                ) : (
                    <ErrorSpan>{status}</ErrorSpan>
                )}
            </TableCol>
            
            {/* <TableCol className='col' size='m' align='center'>
                <span></span>
            </TableCol> */}
        </TableRow>
    )
}

