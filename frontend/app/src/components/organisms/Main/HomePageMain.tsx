import { Riel } from '../../organisms/index';
import { Section, Main } from '../../atoms';


export default function HomePageMain (){
    return (
            <Main className='main--home'>
                <div className="main-col">
                    <Riel title="Breaking on Video Cards"/>
                    <Riel title="Breaking on Video Cards"/>
                    <Section top='none'>
                        <h2>Third Section</h2>
                        <article> 
                        <h3>card</h3>   
                        </article>   
                        <article> 
                        <h3>card</h3>   
                        </article>     
                    </Section>
                </div>
            </Main>
    )
}