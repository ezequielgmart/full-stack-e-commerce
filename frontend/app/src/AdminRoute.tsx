
import { Navigate, Outlet } from 'react-router-dom';
import { useContext } from 'react';
import { AuthContext } from './context/AuthContext';
/**
 * Este componente actúa como un guardián para las rutas de administrador.
 * Comprueba si el usuario está logueado y tiene el rol de 'admin'.
 * Si no, lo redirige a la página de inicio.
 * Si sí, le permite el acceso a las rutas que protege.
 */


export default function AdminRoute() { 
    // TypeScript ahora sabe que 'auth' es de tipo: AuthContextType | null
    const auth = useContext(AuthContext);

    // Por lo tanto, sabe que si 'auth' no es null, TIENE una propiedad 'user'
    // Y que 'user' puede ser un objeto o null.
    // La siguiente línea ahora es 100% segura y correcta para TypeScript.
    if (auth?.user?.role !== 'admin') {
        return <Navigate to="/" replace />;
    }

    return <Outlet />;
}