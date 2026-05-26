import { Sidebar } from "./Sidebar"; import { Topbar } from "./Topbar";
export function PageShell({children}:{children:React.ReactNode}){ return <div className="min-h-screen bg-slate-50"><Sidebar/><main className="ml-72 min-h-screen"><Topbar/><div className="px-8 py-10">{children}</div></main></div> }
