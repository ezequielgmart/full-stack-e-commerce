// atoms
import PrimaryBtnLink from "../../atoms/Button/PrimaryBtnLink"
import CardTitle from "../../atoms/Titles/CardTitle"

// styles
import './cards.css'

export default function SignInCard(){

    return(
        <>
            <div className="generic-card-container">
                <div className="generic-card-body">
                    <CardTitle value="Sign in for the best deals"/>
                    <PrimaryBtnLink href="#" value="Sign in"/>
                </div>
            </div>
        </>
    )
}