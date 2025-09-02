import HomeArticle from "../components/organisms/Article/HomeArticle";
import StorePageTemplate from "../templates/pages/StorePage";

function HomePage() {
    return (
        <>
            <StorePageTemplate>
            <HomeArticle/>
            </StorePageTemplate>
        </>
    );
}

export default HomePage;