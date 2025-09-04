import './spans.css'

// import type { CurrencySpanProps } from '../../../types';


// export default function CurrencySpan({ amount,className }:CurrencySpanProps){
//     const formattedPrice = new Intl.NumberFormat('es-US', {
//         style: 'currency',
//         currency: 'USD',
//     }).format(amount);

//     return (
//         <>
//             <span className={className}>{formattedPrice}</span>
//         </>
//     )
// }

import type { CurrencySpanProps } from '../../types';

export default function CurrencySpan({ amount }:CurrencySpanProps){

    const currencySymbol = "$"
    const amountWithCents = amount.toFixed(2)
    const amountToString = amountWithCents.toString()

    // 2. Separar el precio en la parte entera y los centavos
    const [integerPart, centsPart] = amountToString.split('.');

    return (
        <div className="price-container">
            <span className="price-symbol">{currencySymbol}</span>
            <span className="price-integer">{integerPart}</span>
            <span className="price-cents">{centsPart}</span>
        </div>
    )
}