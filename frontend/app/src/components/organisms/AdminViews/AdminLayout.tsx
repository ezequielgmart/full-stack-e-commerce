import { Outlet } from 'react-router-dom'; // ¡La clave está aquí!
import { Main, AdminAside } from '../../organisms/index';


export default function AdminLayout() {
    // La lista de opciones ahora vive en el layout
    const options = [
        {name:'Dashboard', href:'/admin/dashboard'}, // <-- Rutas corregidas
        {name:'Products', href:'/admin/products'}, 
        {name:'Store', href:'/'}
    ];

    return (
        <Main className='main main--admin'>
            <AdminAside options={options} />
            <div className="content-col">
                {/* Outlet es el marcador de posición donde se renderizará
                    el componente de la ruta hija (Dashboard, Products, etc.) */}
                <Outlet />
            </div>
        </Main>
    );
}