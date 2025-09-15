import { ListItem, Aside, Link } from '../../atoms';

import { AdminList, AsideNavOption, UserNavOption } from '../../molecules';
import { useContext } from 'react';
import { AuthContext } from '../../../context/AuthContext';

import ListContainer from '../../molecules/List/ListContainer';

import { 
    DashboardIcon, 
    ProductsIcon,
    OrdersIcon,
    UsersIcon,
    SalesIcon,
    InvetoryIcon,
    GoToStoreIcon
} from '../../atoms/icons';

import './admin.aside.css'

export default function AdminAside () { 
    
    const auth = useContext(AuthContext);


    const options = [
        {name:'Dashboard', href:'/admin/dashboard', icon:<DashboardIcon/>}, 
        {name:'Products', href:'/admin/products', icon:<ProductsIcon/>}, 
        {name:'Orders', href:'/admin/orders', icon:<OrdersIcon/>}, 
        {name:'Users', href:'/admin/users', icon:<UsersIcon/>}, 
        {name:'Sales', href:'/admin/sales', icon:<SalesIcon/>}, 
        {name:'Inventory', href:'/admin/inventory', icon:<InvetoryIcon/>}, 
        {name:'Store', href:'/', icon:<GoToStoreIcon/>}
    ];

    return (
        <Aside classname='admin--aside-panel'>
            <ListContainer>
                <AdminList>
                    {options.map((item, index)=>(
                        <ListItem key={index}>
                            <AsideNavOption name={item.name} href={item.href} icon={item.icon}>
                            </AsideNavOption>
                        </ListItem>
                    ))}
                </AdminList>
                <UserNavOption username={auth?.user?.username}/>
                    
            </ListContainer>

            

        </Aside>
    )
}