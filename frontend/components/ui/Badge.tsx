import { cn } from "@/lib/utils";
export function Badge({className="", children}:{className?:string; children:React.ReactNode}){ return <span className={cn("inline-flex rounded-full bg-emerald-50 px-3 py-1 text-xs font-semibold text-emerald-700 ring-1 ring-emerald-100", className)}>{children}</span> }
