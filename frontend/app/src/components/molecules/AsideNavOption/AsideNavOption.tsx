import type { ReactNode } from "react";
import { NavLink } from 'react-router-dom';
import './aside.nav.option.css';
import {  Span } from "../../atoms";
 

interface AsideNavOptionProps { 
    name:string; 
    href:string; 
    icon:ReactNode;
}
export default function AsideNavOption({ name, href, icon}:AsideNavOptionProps){ 

    return (
        <>
        <NavLink to={href} 
            // Esto aplica la clase 'active' automáticamente cuando la URL coincide
            className={({ isActive }) => isActive ? 'aside-nav-option active' : 'aside-nav-option'}
        >
            {/* <div className="aside-nav-option-container"> */}
                <div className="icon-container">
                    <Span type="span">
                        {icon}
                    </Span>
                </div>
                <div className="name-container">
                    <Span type="span">
                        {name}
                    </Span>
                </div>
            {/* </div> */}
        </NavLink>
        </>
    ) 
}