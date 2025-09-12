import { TableRow, TableCol } from '../../atoms';


export default function TableRowHeader (){     
    return (      
        
        <thead>                  
            <TableRow className='header'>
                <TableCol className='col col--header' >
                    <span></span>
                </TableCol>
                <TableCol className='col col--header' >
                    <span>Product Name</span>
                </TableCol>
                <TableCol className='col col--header' >
                    <span>Category</span>
                </TableCol>
                <TableCol className='col col--header'  align='center'>
                    <span>Price</span>
                </TableCol>
                <TableCol className='col col--header'  align='center'>
                    <span>Status</span>
                </TableCol>
                
                {/* <TableCol className='col col--header' size='m'>
                    <span></span>
                </TableCol> */}
            </TableRow>
        </thead>
    )
}

