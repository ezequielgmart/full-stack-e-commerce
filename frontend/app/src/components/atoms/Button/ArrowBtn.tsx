import type { CustomArrowProps } from 'react-slick';

export default function ArrowBtn(props:CustomArrowProps){
    const { className, style, onClick } = props

    return(
        <div
            className={className}
            style={{ ...style, display: "block", background: "gray" }}
            onClick={onClick}
        />
    )
}