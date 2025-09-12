import { ProductDetailPage, HomePage } from '../src/pages/index';

import { AdminDashboardView, AdminProductsView, AdminLayout } from './components/organisms';
import { Routes, Route, Navigate } from 'react-router-dom';

import AdminRoute from './AdminRoute';

import './styles/App.css'

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />}/>
      <Route path="/product/details" element={<ProductDetailPage />} /> 

      {/* RUTAS PROTEGIDAS DE ADMINISTRADOR */}
      <Route element={<AdminRoute />}>
        {/* La ruta padre /admin ahora renderiza el LAYOUT */}
        <Route path="/admin" element={<AdminLayout />}>
          
          {/* La ruta 'index' redirige /admin a /admin/dashboard por defecto */}
          <Route index element={<Navigate to="dashboard" replace />} />

          {/* Las rutas hijas se renderizarán DENTRO del <Outlet /> del layout */}
          <Route path="dashboard" element={<AdminDashboardView />} />
          <Route path="products" element={<AdminProductsView />} />
          {/* ... más rutas para Inventory, Orders, etc. ... */}
        </Route>
      </Route>
    </Routes>
  );
}

export default App;

      {/* <Route path="/cart" element={<ShoppingCartPage />} /> 
      <Route path="/account" element={<UserAccountPage />} /> 
      <Route path="/user/address" element={<UserAddressPage />} />  */}