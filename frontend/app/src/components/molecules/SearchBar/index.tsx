
import './shearchbar.css'
import { ButtonLink, Input } from '../../atoms/index.ts';
import { SearchIcon } from '../../atoms/icons.tsx';

import { useNavigate } from 'react-router-dom';

export default function SearchBar() {
    
    const navigate = useNavigate();


    const goToResultsPage = () => {

        navigate('/results');
    };

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault(); // Evita que la página se recargue
        goToResultsPage()
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="search-bar-container" >
                
                <Input 
                    type="text"  
                    variant="primary"
                    size="big" 
                    placeholder="Search..."
                />
                <ButtonLink 
                    href="/results"  
                    variant="ligth"   
                    type="search" 
                    size="medium">
                    <SearchIcon></SearchIcon>
                </ButtonLink>
                
            </div>
        </form>
    );
}



        // <div className="search-bar-container">
        //     <div className='search-bar-col-r'>
        //         <SearchBarTxt/>
        //     </div>
        //     <div className='search-bar-col-l'>
        //         <SearchBtn onClickHandler={handleSearchClick} />
        //     </div>
        // </div>