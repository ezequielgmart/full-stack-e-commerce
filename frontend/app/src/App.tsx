import HomePage from "./pages/HomePage.tsx";
import SearchResultsPage from "./pages/SearchResultsPage.tsx";

import ProductDetailPage from "./pages/ProductDetailsPage.tsx";
import ShoppingCartPage from "./pages/ShoppingCartPage.tsx";
import UserAccountPage from "./pages/AccountPage.tsx";
import UserAddressPage from "./pages/YourAddressPage.tsx";

// import HomePage from './pages/index.ts'

import { Routes, Route } from 'react-router-dom';
import './styles/App.css'
function App() {
  return (
    <Routes>
      {/* Esta ruta manejará http://localhost:5173/ */}
      <Route path="/" element={<HomePage />} /> 
      <Route path="/results" element={<SearchResultsPage />} /> 
      <Route path="/product/details" element={<ProductDetailPage />} /> 
      <Route path="/cart" element={<ShoppingCartPage />} /> 
      <Route path="/account" element={<UserAccountPage />} /> 
      <Route path="/user/address" element={<UserAddressPage />} /> 

    </Routes>
  );
}

export default App;