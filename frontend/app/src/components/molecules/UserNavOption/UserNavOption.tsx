import { Image, Span, Link } from "../../atoms"
import { LogOutIcon } from "../../atoms/icons";
import { useState } from 'react';

import './user.nav.option.css';


interface UserNavOptionProps { 
    username?:string; 

}


export default function UserNavOption ({ username }:UserNavOptionProps) { 
    // Estado para controlar si el menú está abierto o cerrado
    const [isOpen, setIsOpen] = useState(false);

    const handleLogout = () => {
        // Aquí lógica para cerrar sesión del AuthContext
        alert('CLose sesion')
    };

    return(
        <div className="user-nav-option">
            <div className="user-nav-option-user-container">
                <button className="profile-trigger" 
                    onClick={() => setIsOpen(true)}  // Abre el menú
                    onMouseLeave={() => setIsOpen(false)}>
                    
                <img src="/avatar.jpg" className="avatar-img"/>
                <Span type="span">{username}</Span>
                
                </button>
            </div>
            {isOpen && (
                <div className="dropdown-menu">
                    <Link href="/admin/profile">Mi Perfil</Link>
                    <button onClick={handleLogout} className="logout-button">
                        <LogOutIcon />
                        <span>Log out</span>
                    </button>
                </div>
            )}
            {/* <div className="user-nav-option-actions">
                
                <Span>
                    <LogOutIcon/>
                </Span>
            </div> */}
        </div>
    )
}