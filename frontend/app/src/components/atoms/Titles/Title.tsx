import type { GenericSpanProps } from "../../../types";
export default function TitleH({ value, className}:GenericSpanProps){

    return (
        <h1 className={className}>{value}</h1>
    )
}