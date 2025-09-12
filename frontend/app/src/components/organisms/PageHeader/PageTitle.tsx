import type { ReactNode } from "react";

interface TitleProps { 

    children:ReactNode
}

export default function PageTitle({ children }:TitleProps){

    return (
        <title>
            { children }
        </title>
    );
}
