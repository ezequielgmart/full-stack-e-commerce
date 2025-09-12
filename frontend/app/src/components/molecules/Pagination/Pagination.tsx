import { Button } from "../../atoms";
import './pagination.css'
interface Info { 

    total_items: number;
    total_pages: number;
    per_page: number;

}
interface PaginationProps { 

    info:Info;
    currentPage:number;
    onPageChange:(arg0: number) => void;
}

export default function Pagination ({ info, currentPage, onPageChange }:PaginationProps) { 

    const totalPages = info.total_pages;

    // Lógica para crear los números de página
    const pageNumbers = [];
    for (let i = 1; i <= totalPages; i++) {
        pageNumbers.push(i);
    }

    return (
        <nav className="pagination-nav nav--horizontal">

                {
                    pageNumbers.map((page)=>(
                        
                        <Button 
                            key={page}
                            // Cuando haces clic, llama a la función que le pasó el padre
                            onClick={() => onPageChange(page)}

                            customClassName={currentPage === page ? 'pagination-btn btn--active' : 'pagination-btn'}
                        >

                        {page}
                        
                        </Button>

                    ))
                }


        </nav>
    )
}