import Button from  './index';

import type { BtnProps } from "../../../types";

export default function PrimaryButton ({  children, onClick }: BtnProps){ 

    return (
        <Button variant='primary'  size='medium' onClick={onClick}>
            {children}
        </Button>
     )
}