import type { ReactNode } from 'react';
import './list.item.css';

interface ListItemProps { 
    children:ReactNode;
}
export default function ListItem({ children }:ListItemProps){
    return (
        <li>{children}</li>
    )
}