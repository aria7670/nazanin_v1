import { create } from 'zustand'
import { persist } from 'zustand/middleware'

export interface User {
  id: string
  name: string
  email: string
  role: 'admin' | 'moderator' | 'user'
  avatar?: string
}

interface AuthState {
  user: User | null
  isAuthenticated: boolean
  login: (email: string, password: string) => Promise<boolean>
  logout: () => void
  updateUser: (user: Partial<User>) => void
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      user: null,
      isAuthenticated: false,
      
      login: async (email: string, password: string) => {
        // Mock authentication - در پروژه واقعی با API سرور ارتباط برقرار می‌شود
        if (email === 'admin@nazanin.com' && password === 'admin123') {
          const user: User = {
            id: '1',
            name: 'مدیر سیستم',
            email: email,
            role: 'admin',
          }
          set({ user, isAuthenticated: true })
          return true
        }
        return false
      },
      
      logout: () => {
        set({ user: null, isAuthenticated: false })
      },
      
      updateUser: (updatedData: Partial<User>) => {
        set((state) => ({
          user: state.user ? { ...state.user, ...updatedData } : null,
        }))
      },
    }),
    {
      name: 'auth-storage',
    }
  )
)
