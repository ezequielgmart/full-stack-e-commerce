import { ListItem, Link, Aside } from '../../atoms';
import { AdminList } from '../../molecules';
import { useContext } from 'react';
import { AuthContext } from '../../../context/AuthContext';
import ListContainer from '../../molecules/List/ListContainer';

interface Option { 
    name: string;
}

interface ListOptions { 
    options:Array<Option>
}
export default function AdminAside ({ options }: ListOptions) { 
    
    const auth = useContext(AuthContext);
    
    return (
        <Aside classname='admin--aside-panel'>
            <ListContainer>
                <AdminList>
                    <Link href='/'>
                            {auth?.user?.username}
                    </Link>
                    {options.map((item, index)=>(
                        <ListItem key={index}>
                            <Link href={item.href}>
                                    {item.name}
                            </Link>
                        </ListItem>
                    ))}
                </AdminList>
            </ListContainer>
        </Aside>
    )
}