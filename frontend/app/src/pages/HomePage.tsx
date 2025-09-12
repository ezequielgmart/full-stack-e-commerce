
/* components */
import { NavBar, PageHeader, PageTitle, Footer } from "../components/organisms/index";

/* admin components */

import HomePageMain from "../components/organisms/Main/HomePageMain";
import Page from "./Template";


export default function HomePage() {  
    // const TestUser = {
    //     user_id: "adasdasd",
    //     username: "TestSudo",
    //     role: "admin" 
    // };
    
    // El estado específico de esta página
    /* esto eventualmente tiene que tomar el estado global de la aplicaicon y ver que usuario esta logueado, verificarlo, si tiene un token valido */
    // const [user, setUser] = useState<User>(TestUser);


    return (
        <Page>
        <PageTitle>Welcome to Eshop | Home</PageTitle>
        <PageHeader>
            <NavBar></NavBar>
        </PageHeader>
        <HomePageMain></HomePageMain>
            <Footer></Footer>
        </Page>
                
    );

}


