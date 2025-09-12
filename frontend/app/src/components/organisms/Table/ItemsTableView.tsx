
// types
import type { ProductsApiResponse, Product } from '../../../types';

// consts
import { URL_ROOT } from '../../../utils/constants';

// react functions
import { useState, useMemo } from 'react'; // 1. Importamos useState y useMemo

// atoms
import { Table, Section, Span } from '../../atoms'

// molecules
import { TableHeader, TableProductRow, TableRowHeader, Pagination, TableController } from "../../molecules";
import { useFetch } from "../../../hooks/custom";
import { ArrowDownIcon } from '../../atoms/icons';


const limit = 10;
const endpoint = 'products';


export default function ProductsTableView(){ 

    // PASO 1: Añadir estado para la página actual
    const [currentPage, setCurrentPage] = useState(1);

    // PASO 2: Hacer la URL dinámica
    // Calculamos el 'offset' basado en la página actual
    const offset = (currentPage - 1) * limit;
    // Creamos la URL completa, que ahora cambiará cada vez que 'currentPage' cambie
    const url = `${URL_ROOT}${endpoint}/?limit=${limit}&offset=${offset}`;

    // PASO 3: Conectar useFetch con la URL dinámica
    // No hay que cambiar nada aquí. ¡Simplemente funcionará!
    const { data: apiResponse, loading, error } = useFetch<ProductsApiResponse>(url);

    // Extraemos los datos como ya lo hacías
    const products = apiResponse?.data;
    const paginationInfo = apiResponse?.info; // Necesitamos esto para el componente de paginación
        
    // PASO 4: Crear la función de Callback
    const handlePageChange = (newPage: number) => {
        setCurrentPage(newPage);
        // ¡Eso es todo! El resto de la magia ocurre sola.
    };

    // Si está cargando, mostramos un mensaje
    if (loading) {
        return <div>Cargando productos...</div>
    }
    // Si hay un error, lo mostramos
    if (error) {
        return <div>Error: {error.message}</div>
    }

    return (
        <Section top='none' background='secondary' width='s' position='center' border='none' bottom='s'>
            <TableHeader/>
            <div className='table-controllers-container'>
                <TableController >
                    <span>Showing {products?.length ?? 0}</span>
                </TableController>
            </div>
            <Table>
                <TableRowHeader />

                <tbody>
                    {products?.map((product: Product, index) => (
                        <TableProductRow number={index} data={product}>
                        </TableProductRow>
                    ))} 
                </tbody>
            </Table>
            <div className='pagination-component-container'>
                {paginationInfo && (
                    <Pagination 
                        info={paginationInfo} 
                        currentPage={currentPage}
                        onPageChange={handlePageChange}
                    />
                )}
            </div>
        </Section >
    )
}