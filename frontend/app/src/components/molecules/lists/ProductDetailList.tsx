// import './lists.css';
// import Span from '../../atoms/Span';

// export default function ProductDetailList (){ 
//     const listItems = [
//         'NVIDIA GeForce RTX 40 Series: NVIDIA GeForce RTX 4080 Laptop GPU 12GB GDDR6.Adapter : 280W, Battery Li Polymer : 99Wh',
//         'Intel 13th Gen Ready: i7-13700H Processor 5.0 GHz',
//         'DDR5 Ready: DDR5 4800 8GB2 (16GB), 1TB Storage (Gen4 M.2 SSD)',
//         'Cutting-Edge Display: 17.3" Thin Bezel FHD 1920x1080, 360Hz, 100% sRGB, TÜV Rheinland Certified',
//         'Next Gen Interface: Windows 11 Home AD, Intel Wi-Fi 6E, Bluetooth V5.2',
//         'Dynamic Audio: Built-in Microphone, 2x 2W Speakers',
//         'IO: 1x Thunderbolt 4 (Supports Power Delivery), 1x HDMI 2.1, 1x Mini DP 1.4 (120Hz), 2x USB 3.2 Gen1 (Type-A), 1x RJ45, 1x Audio Combo Jack, 1x DC In'
//     ]
//     return (
//         <ul>
//             {listItems.map((element, index) => (
//             <li key={index}> {/* <-- CORRECCIÓN: Se añade la key */}
//                 <Span className="component-span-s" value={element} />
//             </li>
//             ))}
//         </ul>
//     )
// }