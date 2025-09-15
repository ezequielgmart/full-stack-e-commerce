import { 
  FiMapPin, 
  FiSearch, 
  FiShoppingCart,  
  FiChevronDown,
  FiGrid,
  FiPackage,
  FiTruck,
  FiUsers,
  FiBarChart2,
  FiArchive,
  FiExternalLink,
  FiPower,
  FiEdit 

} from "react-icons/fi";

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

/* admin aside icons */
export function DashboardIcon({ className }:IconsProps){
  return (
    <FiGrid  className={className}/>
  )
}

export function ProductsIcon({ className }:IconsProps){
  return (
    <FiPackage  className={className}/>
  )
}

export function OrdersIcon({ className }:IconsProps){
  return (
    <FiTruck  className={className}/>
  )
}

export function UsersIcon({ className }:IconsProps){
  return (
    <FiUsers  className={className}/>
  )
}

export function SalesIcon({ className }:IconsProps){
  return (
    <FiBarChart2  className={className}/>
  )
}

export function InvetoryIcon({ className }:IconsProps){
  return (
    <FiArchive  className={className}/>
  )
}

export function GoToStoreIcon({ className }:IconsProps){
  return (
    <FiExternalLink  className={className}/>
  )
}

export function LogOutIcon({ className }:IconsProps){
  return (
    <FiPower   className={className}/>
  )
}

export function EditIcon({ className }:IconsProps){
  return (
    <FiEdit   className={className}/>
  )
}

