
export const generateClassName = (tag:string, variant:string, size:string) =>{
    // title title--primary title--big
    const result = `${tag} ${tag}--${variant} ${tag}--${size}`
    return result
} 

