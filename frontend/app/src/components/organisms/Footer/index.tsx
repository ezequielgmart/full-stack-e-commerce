// // NOTE: 
// // archivo index.ts 
// // que lo exporta, haciendo las importaciones más limpias.
import './footer.css'

export default function Footer(){
    return(
        <>
            <footer className='footer footer-main'>
                <ul>
                    <h2>Footer</h2>
                    <li><a href="#">Home</a></li>
                </ul>
            </footer>
        </>
    )
}