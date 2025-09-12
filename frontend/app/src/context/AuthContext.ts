import { createContext } from 'react';

// Define tu tipo User, que ya tienes
export interface User {
    user_id: string;
    username: string; 
    role: "admin" | "customer";
}

// Ahora, define la forma del valor del contexto
export interface AuthContextType {
    user: User | null; // El usuario puede ser un objeto User o null si no está logueado
    login: (userData: User) => void; // Una función para hacer login
    logout: () => void; // Una función para hacer logout
}


// Creamos el contexto. El 'null' es el valor por defecto que tendría si
// un componente intenta usarlo sin estar envuelto en un Provider.
// Le decimos que el valor puede ser AuthContextType O null, y que empieza siendo null.
export const AuthContext = createContext<AuthContextType | null>(null);