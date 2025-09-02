
import './rows.css'

import type { PropsWithChildren } from "react";
export default function HomeArticleRow({children}:PropsWithChildren){


    return (
        // cambiar el nombre de la clase
        <section className="home-section-row">
            {children}
        </section>


    );

}