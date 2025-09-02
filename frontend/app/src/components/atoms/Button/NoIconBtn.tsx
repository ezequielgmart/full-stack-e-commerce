import './buttons.css'

import type { BtnPropsNoClass } from '../../../types';
// Aplica la interfaz a las props del componente
// esto ira dentro del div de cada componente del navbar
export default function NoIconBtn({ className, value, onClick }: BtnPropsNoClass) {
    return (

        <button  className={className}  onClick={onClick} >{value}</button>

    );
}
