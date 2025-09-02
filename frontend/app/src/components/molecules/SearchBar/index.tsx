
import './shearchbar.css'
import SearchBarTxt from "../../atoms/Input/SearchBar.tsx";
import SearchBtn from "../../atoms/Button/SearchBtn.tsx";
import { useNavigate } from 'react-router-dom';

function SearchBar() {
    
    const navigate = useNavigate();

    // Manejador del evento de click del botón
    const handleSearchClick = () => {
        goToResultsPage()
    };

    const goToResultsPage = () => {

        navigate('/results');
    };

    return (
        <div className="search-bar-container">
            <SearchBarTxt/>
            <SearchBtn onClickHandler={handleSearchClick} />
            
        </div>
    );
}

export default SearchBar;


        // <div className="search-bar-container">
        //     <div className='search-bar-col-r'>
        //         <SearchBarTxt/>
        //     </div>
        //     <div className='search-bar-col-l'>
        //         <SearchBtn onClickHandler={handleSearchClick} />
        //     </div>
        // </div>