import type { BtnLinkProps } from "../../../types";

import './buttons.css'

export default function PrimaryBtnLink({ href, value}: BtnLinkProps) {
    return (
        <a className="primary-btn" href={href}>
            <div className="primary-btn-container">
                <span className="primary-btn-span"> 
                    {value}
                </span>
            </div>
        </a>
    );
}

