'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import {
  LayoutDashboard,
  Users,
  Package,
  ShoppingCart,
  Settings,
  BarChart3,
  FileText,
  Bell,
  Tag,
} from 'lucide-react'

const menuItems = [
  {
    title: 'داشبورد',
    icon: LayoutDashboard,
    href: '/dashboard',
  },
  {
    title: 'کاربران',
    icon: Users,
    href: '/dashboard/users',
  },
  {
    title: 'محصولات',
    icon: Package,
    href: '/dashboard/products',
  },
  {
    title: 'سفارشات',
    icon: ShoppingCart,
    href: '/dashboard/orders',
  },
  {
    title: 'دسته‌بندی‌ها',
    icon: Tag,
    href: '/dashboard/categories',
  },
  {
    title: 'گزارشات',
    icon: BarChart3,
    href: '/dashboard/reports',
  },
  {
    title: 'مقالات',
    icon: FileText,
    href: '/dashboard/posts',
  },
  {
    title: 'اعلان‌ها',
    icon: Bell,
    href: '/dashboard/notifications',
  },
  {
    title: 'تنظیمات',
    icon: Settings,
    href: '/dashboard/settings',
  },
]

export default function Sidebar() {
  const pathname = usePathname()

  return (
    <aside className="fixed top-0 right-0 z-40 w-64 h-screen transition-transform bg-white border-l border-gray-200 shadow-lg">
      <div className="h-full px-3 py-4 overflow-y-auto">
        {/* Logo */}
        <div className="flex items-center justify-center mb-8 mt-4">
          <div className="bg-gradient-to-br from-blue-600 to-indigo-600 rounded-xl p-3 shadow-lg">
            <LayoutDashboard className="h-8 w-8 text-white" />
          </div>
          <span className="mr-3 text-xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
            پنل نازنین
          </span>
        </div>

        {/* Menu */}
        <ul className="space-y-2 font-medium">
          {menuItems.map((item) => {
            const Icon = item.icon
            const isActive = pathname === item.href
            
            return (
              <li key={item.href}>
                <Link
                  href={item.href}
                  className={`flex items-center p-3 rounded-lg transition-all duration-200 ${
                    isActive
                      ? 'bg-gradient-to-r from-blue-600 to-indigo-600 text-white shadow-md'
                      : 'text-gray-700 hover:bg-gray-100'
                  }`}
                >
                  <Icon className={`h-5 w-5 ml-3 ${isActive ? 'text-white' : 'text-gray-500'}`} />
                  <span className="flex-1">{item.title}</span>
                </Link>
              </li>
            )
          })}
        </ul>
      </div>
    </aside>
  )
}
