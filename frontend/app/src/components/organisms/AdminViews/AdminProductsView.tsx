
import { Section } from '../../atoms';
import { ProductsTableView } from '../index';
import { PageHeaderContainer } from '../../molecules';

export default function AdminProductsView (){


    return (
        <>
            <title>Eshop Admin | Products</title>
            <Section top='none' background='light'>
                <PageHeaderContainer title='Products'></PageHeaderContainer>
                <ProductsTableView></ProductsTableView>
            </Section>
        </>
     
    )
}