import { NavBar, Main } from "../components/organisms/index";

export default function HomePage() {    
    
    return (
        <>
            <NavBar></NavBar>
            <Main>
                <aside className='card-one'>
                    <h2>Aside</h2>
                </aside>
                <article className='card-two'>
                    <h2>Article</h2>
                </article>
            </Main>

        </>
    );
}
