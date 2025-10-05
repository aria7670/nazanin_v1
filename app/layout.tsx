import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Nazanin Admin Panel',
  description: 'Modern and powerful admin panel',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="fa" dir="rtl">
      <body>{children}</body>
    </html>
  )
}
