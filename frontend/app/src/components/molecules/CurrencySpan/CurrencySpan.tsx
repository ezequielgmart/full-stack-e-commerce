import './index.css'

interface CurrencySpanProps { 
    amount:number;

}
export default function CurrencySpan({amount}:CurrencySpanProps){ 
    const amountFixed = amount.toFixed(2)
    const amountToString = amountFixed.toString()

    const [integerPart, centsPart] = amountToString.split('.');

    const currencyFormat = new Intl.NumberFormat('es-DO', {
        style: 'decimal'
    });

    const symbol = "$"
    return (
        <div className='price-display'>
                <span className='price-display__symbol'>{symbol}</span>
                <span className='price-display__integer'>{currencyFormat.format(parseInt(integerPart))}</span>
                <span className='price-display__cents'>{centsPart}</span>

        </div>
    )
}