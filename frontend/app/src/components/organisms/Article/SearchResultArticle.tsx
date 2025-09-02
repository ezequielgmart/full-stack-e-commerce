
import ResultProductCard from '../../molecules/Card/ResultProductCard';
import ResultPageFooter from '../../molecules/PageFooter/ResultPageFooter';

import './articles.css';

export default function SearchResultArticle(){

    return (
        <article className="items-list-article">
            <div className="items-list-header">
                <h4>Results</h4>
            </div>
            <ResultProductCard/>
            <ResultProductCard/>
            <ResultProductCard/>
            <ResultProductCard/>
            <ResultPageFooter/>
        </article>
    );
}
