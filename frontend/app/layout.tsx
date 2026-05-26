import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "AirLens | Climate Intelligence Workspace", description: "Climate-tech research and outreach intelligence platform" };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) { return <html lang="en"><body>{children}</body></html>; }
