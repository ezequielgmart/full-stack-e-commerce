import type { ReactNode } from "react"
interface PageProps { 

    children:ReactNode
}

export default function Page({children}:PageProps){
    return (
        <div className="page-container">
            {children}
        </div>
    )
}