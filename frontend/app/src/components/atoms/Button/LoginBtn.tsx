import type { BtnProps } from "../../../types";

import './buttons.css'
export function LoginBtn({ value, onClick }: BtnProps) {
    return (
        <>
            <button 
                id="btn-login" 
                className="btn-login"
                onClick={onClick}
                >
                    {value}
            </button>
        </>
    );
}

