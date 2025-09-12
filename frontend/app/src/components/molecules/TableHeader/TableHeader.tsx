
import { Title, Article, PrimaryButton, Span } from "../../atoms";
import SearchInput from "../SearchInput/SearchInput";
import './table.header.css';

interface TableHeaderProps {
    total_items:number;    
}

export default function TableHeader() { 
    return (
        
        <Article 
            top='none' 
            background='light' 
            position='center' 
            padding='s'
            border='none'
        >

                <div className='content-header-col cols--6 background--secondary'>
                    <div className="header-search-input">
                        <SearchInput></SearchInput>
                    </div>
                    <div className="header-btn">
                        <PrimaryButton>New product</PrimaryButton>
                    </div>
                </div>
                {/* <div className='content-header-col'>
                    <Title  level='3' size='small' variant='ligth'>Showing ({total_items}) items</Title>
                </div> */}

        </Article>
    )
}