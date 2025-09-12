
import { Title, Section } from '../../atoms';

import './page.header.css';


interface PageHeaderContainerProps { 
    title:string;
}
export default function PageHeaderContainer ({ title }:PageHeaderContainerProps){


    return (
        <Section 
            top='none' 
            background='light' 
            width='s' 
            position='center' 
            padding='s'
            border='none'
        >
            <Title  level='1' size='big' variant='ligth'>{title}</Title>


        </Section>
     
    )
}