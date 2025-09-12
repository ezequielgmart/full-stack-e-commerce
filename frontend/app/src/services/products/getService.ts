import { ApiResponseExample } from "./data";
import type { Product, ProductsApiResponse } from "../../types";

export const GetAllProducts = async (): Promise<ProductsApiResponse> => {
    console.log("Llamando a la API para obtener todos los productos...");

    return new Promise(resolve => {
        setTimeout(() => {
            console.log("...Datos recibidos de la API.");
            resolve(ApiResponseExample);
        }, 500); // Simula un retraso de 500 milisegundos
    });
};

export const GetProductsByCategory = async (category: string): Promise<Product[]> => {
    console.log(`Llamando a la API para la categoría: ${category}...`);

    return new Promise(resolve => {
        setTimeout(() => {
            const allProducts = ApiResponseExample.data;

            // Usamos .filter() para buscar dinámicamente en todos los productos
            const filteredProducts = allProducts.filter(
                product => product.category_name.toLowerCase() === category.toLowerCase()
            );

            console.log(`...Se encontraron ${filteredProducts.length} productos.`);
            resolve(filteredProducts);
        }, 500);
    });
};