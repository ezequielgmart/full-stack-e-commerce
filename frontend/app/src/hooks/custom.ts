import { useState, useEffect } from 'react';



// // (Tus tipos de Data y ErrorType aquí)
// type Data<T> = T | null;
// type ErrorType = Error | null; 


// Interfaz para el valor de retorno del hook
interface FetchResult<T> {
    data: T | null;
    loading: boolean;
    error: Error | null;
}

export function useFetch<T>(url: string): FetchResult<T> { 
    const [data, setData] = useState<T | null>(null);
    const [loading, setLoading] = useState(true); // Inicia en true
    const [error, setError] = useState<Error | null>(null);

    useEffect(() => {
        // Para prevenir memory leaks
        const controller = new AbortController();
        const signal = controller.signal;

        const fetchData = async () => {
            setLoading(true); // También ponemos true aquí por si la url cambia
            try { 
                const response = await fetch(url, { signal }); // Pasamos el 'signal'

                if (!response.ok) { 
                    throw new Error(`Error ${response.status}: ${response.statusText}`);
                }

                const jsonData: T = await response.json();
                setData(jsonData);
                setError(null); // Limpiamos errores anteriores si la nueva petición es exitosa

            } catch (err) {
                if (err instanceof Error && err.name !== 'AbortError') {
                    setError(err);
                }
            } finally { 
                setLoading(false);
            }
        };

        fetchData();

        // Función de limpieza: se ejecuta si el componente se desmonta o la url cambia
        return () => {
            controller.abort();
        };

    }, [url]); // url está en las dependencias

    return { data, loading, error };
}