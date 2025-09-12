import { FiMapPin, FiSearch, FiShoppingCart,  FiChevronDown } from "react-icons/fi";

interface IconsProps { 
  className?:string;
}
export function AddressIcon({ className }:IconsProps){
    
  return (

    <FiMapPin className={className}/>

  );
}

export function SearchIcon({ className }:IconsProps){
  return (
    <FiSearch className={className}/>
  )
}

export function ShoppingCart({ className }:IconsProps){
  return (
    <FiShoppingCart className={className}/>
  )
}

export function ArrowDownIcon({ className }:IconsProps){
  return (
    <FiChevronDown  className={className}/>
  )
}