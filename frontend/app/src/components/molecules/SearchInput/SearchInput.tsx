
import { Input } from '../../atoms'; // Asumiendo que viene de tu barrel file
import { SearchIcon } from '../../atoms/icons'; // La ruta a tu icono
import './search.input.css'

export default function SearchInput() {
  return (
    <div className="search-input-container">
      <SearchIcon className="search-input-icon" />
      <Input 
        type="text" customClassName='search-input-field' placeholder="Search by name..." 
      />
    </div>
  );
}