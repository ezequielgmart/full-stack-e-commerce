import type { PropsWithChildren } from 'react';
import './articles.css';

export default function RootTwoCols({children}:PropsWithChildren){

    return (
        <main className="root-main-two-cols">
            {children}
            
        </main>
    );
}
