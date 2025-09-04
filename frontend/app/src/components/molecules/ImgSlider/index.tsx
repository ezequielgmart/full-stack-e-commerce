// // imports
// import Slider from "react-slick";

// // css files
// import "slick-carousel/slick/slick.css";
// import "slick-carousel/slick/slick-theme.css";
// import './slider.css' // my css file 

// // components
// import SliderImg from "../../atoms/Imgs/SliderImg";
// import ArrowBtn from "../../atoms/Button/ArrowBtn";

// function SimpleSlider() {
//   const settings = {
//     dots: false,
//     infinite: true,
//     speed: 500,
//     slidesToShow: 1,
//     slidesToScroll: 1,
//     // --- properties added for auto play ---
//     autoplay: true,
//     autoplaySpeed: 10000, // change the img 
//     // --------- arrows btn settings ---------------------------
//     nextArrow: <ArrowBtn/>,
//     prevArrow:<ArrowBtn/>,
//   };

//   const imgs = [
//     "public/Intel-Arc.jpg",
//     "public/mac_info.jpg",
//     "public/razer-blade.jpg"
//   ]

//   return (
//     <div className="slider-container">
//         <Slider {...settings}>
//             {imgs.map((imgUrl, index)=>(

//                 <SliderImg key={index} src={imgUrl}/>

//             ))}
//         </Slider>
//     </div>
//   );
// }

// export default SimpleSlider;