// import HomeArticle from "../components/organisms/Article/HomeArticle";
import StorePageTemplate from "../templates/pages/StorePage";

import SearchResultArticle from "../components/organisms/Article/SearchResultArticle";
import FiltersAside from "../components/organisms/Aside/SearchResultsAside";
import SearchResultHeader from "../components/organisms/PageHeader/SearchResultsHeader";

import RootTwoCols from "../components/organisms/Article/RootTwoCols";

export default function SearchResultsPage() {
    return (
        <>
            <StorePageTemplate>
                <SearchResultHeader/>
                <RootTwoCols>
                    <FiltersAside/>
                    <SearchResultArticle/>
                </RootTwoCols>
            </StorePageTemplate>
        </>
    );
}
