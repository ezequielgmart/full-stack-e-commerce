import { Title } from "../../atoms/index.ts";
import ProductCard from "../Cards/ProductCard";
import { useFetch } from "../../../hooks/custom.ts";
import { URL_ROOT } from "../../../utils/constants.ts";
import type { ProductsApiResponse, Product } from "../../../types"; // Importamos el tipo de la respuesta
import './riels.css';

const page = 5
const endpoint = 'products'
const url = `${URL_ROOT}${endpoint}/?limit=${page}`;

interface RielProps { 
    title: string; 
}
export default function Riel({ title }:RielProps) {
    // 1. Especificamos el tipo que esperamos recibir del hook
    const { data: apiResponse, error, loading } = useFetch<ProductsApiResponse>(url);

    if (loading) {
        return <div>Cargando productos del riel...</div>;
    }
    
    if (error) { 
        return <div>¡Upps! Ocurrió un error: {error.message}</div>;
    }

    // 2. Extraemos la lista de productos del objeto de respuesta
    const products = apiResponse?.data; // Usamos optional chaining (?.) por si apiResponse es null

    // 3. Añadimos una comprobación por si no hay productos
    if (!loading) {
        if (!products || products.length === 0 ){

            return <div>No se encontraron productos.</div>
        }
    }

    return (
        <section className="riel">
            <div className="riel-header">
               <Title 
               level={'3'} 
               size='medium' 
               variant='neutral'
               weight='bold'>{title}</Title> 
            </div>
            <div className="riel-body-container">
                {/* Ahora sí hacemos el map sobre el array correcto */}
                {products.map((product: Product) => (
                    <ProductCard 
                        key={product.product_id}
                        product={product}
                    />
                ))}
            </div>
        </section>
    );
}