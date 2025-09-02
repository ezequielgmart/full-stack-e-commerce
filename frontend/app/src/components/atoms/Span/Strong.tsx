

import type { GenericTxtProps } from "../../../types";

export default function Strong({className, value}:GenericTxtProps){
    
  return (

    <strong className={className}>{value}</strong>

  );
}

