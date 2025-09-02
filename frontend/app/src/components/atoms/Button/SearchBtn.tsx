import { FiSearch } from "react-icons/fi";

// Define la interfaz
interface SearchBtnProps {
    onClickHandler:() => void;

}

// Aplica la interfaz a las props del componente
// esto ira dentro del div de cada componente del navbar
export default function SearchBtn({ onClickHandler }: SearchBtnProps) {
    return (
        <>
            <button  className="btn-icon-white"  onClick={onClickHandler} >
            <FiSearch />
            </button>
        </>
    );
}
