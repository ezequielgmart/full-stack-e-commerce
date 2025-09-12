import { useState  } from 'react';
import type { ReactNode  } from 'react';
import { AuthContext } from './AuthContext';

import type { User, AuthContextType } from './AuthContext'

interface AuthProviderProps { 
    children:ReactNode
}

// Este componente envolverá a toda tu aplicación o a una parte de ella
export function AuthProvider({ children }:AuthProviderProps) {
    const mockUser: User = {
        user_id: "asdasdasd-asda4sd5ca1sc8asc",
        username: "MockAdmin", 
        role: "admin"
    }

    const [user, setUser] = useState<User | null>(mockUser);

    const login = (userData: User) => setUser(userData);
    const logout = () => setUser(null);

    // const value: AuthContextType = { user, login, logout };
    const value: AuthContextType = { user, login, logout };

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
}