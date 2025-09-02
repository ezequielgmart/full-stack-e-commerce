
// import SimpleSlider from "../../molecules/ImgSlider";
import HomeArticleRow from "../Rows/HomeArticleRow";
import CategoryProductCard from "../../molecules/Card/CategoryProductCard";
import SponsoredProductCard from "../../molecules/Card/SponsorProductCard";

import HorizontalCarrousel from "../../molecules/Carrousel/HorizontalCarrousel";
// import SignInCard from "../../molecules/Card/SignInCard";

import './articles.css';
function HomeArticle(){

    const ProductsList = [
    { itemName: "Acer Nitro 5", ImgSrc: "products/Acer Nitro 5/1.jpg" },
    { itemName: "Acer Predator Helios 18", ImgSrc: "products/Acer Predator Helios 18/2.jpg" },
    { itemName: "ASUS TUF Gaming A15", ImgSrc: "products/ASUS TUF Gaming A15/5.jpg" },
    { itemName: "DELL ALIENWARE M16", ImgSrc: "products/Dell AlienWare m16/1.jpg" }
    ];

    const SponsoredProduct = {

      itemName: "MacBook Pro 14",
      description: "High-performance laptop with M3 Pro chip, 18GB RAM, and 512GB SSD.",
      unitPrice: 2199.99,
      ImgSrc:'/MacBook Pro 14/1.jpg',
      stock: 50,
      images: [
        "/MacBook Pro 14/1.jpg",
        "/MacBook Pro 14/2.jpg",
        "/MacBook Pro 14/3.jpg",
        "/MacBook Pro 14/4.jpg",
        "/MacBook Pro 14/5.jpg"
    ]
    }

    // const SponsoredProduct = {

    //   "product_id": "b30a1c8f-28c0-43f5-a8e9-d757d54402a1",
    //   "name": "MacBook Pro 14",
    //   "description": "High-performance laptop with M3 Pro chip, 18GB RAM, and 512GB SSD.",
    //   "unit_price": 2199.99,
    //   "stock": 50,
    //   "category_name": "Laptops",
    //   "images": [
    //     "/MacBook Pro 14/1.jpg",
    //     "/MacBook Pro 14/2.jpg",
    //     "/MacBook Pro 14/3.jpg",
    //     "/MacBook Pro 14/4.jpg",
    //     "/MacBook Pro 14/5.jpg"

    // }

    return (
        <article className="main-article">
            {/* <SimpleSlider></SimpleSlider> */}
            
            {/* <SimpleSlider/> */}
            <HomeArticleRow>
                <CategoryProductCard categoryTitle="On Gaming Laptops" data={ProductsList}/>
                <CategoryProductCard categoryTitle="Brand new on Office Laptops" data={ProductsList}/>
                <CategoryProductCard categoryTitle="Trending on Graphic Cards" data={ProductsList}/>
                {/* <SignInCard/> */}
                <SponsoredProductCard data={SponsoredProduct}/>
                
            </HomeArticleRow>
            <HorizontalCarrousel value="Products you migth like"></HorizontalCarrousel>
            <HomeArticleRow>
                <CategoryProductCard categoryTitle="On Gaming Laptops" data={ProductsList}/>
                <CategoryProductCard categoryTitle="Brand new on Office Laptops" data={ProductsList}/>
                <CategoryProductCard categoryTitle="Trending on Graphic Cards" data={ProductsList}/>
                <CategoryProductCard categoryTitle="Trending on Graphic Cards" data={ProductsList}/>

            </HomeArticleRow>
            
        </article>
    );
}

export default HomeArticle