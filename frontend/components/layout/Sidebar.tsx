"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  Activity,
  BookOpen,
  ChartNoAxesColumn,
  Database,
  FileText,
  FlaskConical,
  Leaf,
  Megaphone,
  NotebookPen,
  Settings2,
  UsersRound,
  Wind,
  type LucideIcon,
} from "lucide-react";
import { Badge } from "@/components/ui/Badge";
import type { NavigationItem } from "@/lib/types";
import { cn } from "@/lib/utils";

type NavigationLink = NavigationItem & {
  icon: LucideIcon;
};

const navigation: NavigationLink[] = [
  { href: "/", label: "Overview", icon: Activity },
  { href: "/datasets", label: "Datasets", icon: Database },
  { href: "/dashboard", label: "Dashboard", icon: ChartNoAxesColumn },
  { href: "/research-brief", label: "Research Brief", icon: BookOpen },
  { href: "/content-studio", label: "Content Studio", icon: Megaphone },
  { href: "/outreach", label: "Outreach CRM", icon: UsersRound },
  { href: "/research-log", label: "Research Log", icon: NotebookPen },
  { href: "/biofiltration", label: "Biofiltration", icon: FlaskConical },
  { href: "/reports", label: "Reports", icon: FileText },
  { href: "/settings", label: "Settings", icon: Settings2 },
];

function Brand() {
  return (
    <Link href="/" className="flex items-center gap-3" aria-label="AirLens overview">
      <span className="flex size-11 items-center justify-center rounded-2xl bg-emerald-500 text-white shadow-lg shadow-emerald-950/30">
        <Wind className="size-6" />
      </span>
      <span>
        <span className="block text-lg font-semibold tracking-tight text-white">
          AirLens
        </span>
        <span className="block text-xs text-slate-400">Climate intelligence</span>
      </span>
    </Link>
  );
}

function NavigationLinks({ compact = false }: { compact?: boolean }) {
  const pathname = usePathname();

  return navigation.map(({ href, icon: Icon, label }) => {
    const isActive = pathname === href;

    return (
      <Link
        key={href}
        href={href}
        className={cn(
          "flex items-center gap-3 rounded-xl text-sm font-medium transition-colors",
          compact ? "shrink-0 px-3 py-2.5" : "px-3 py-2.5",
          isActive
            ? "bg-emerald-500/15 text-emerald-300"
            : "text-slate-400 hover:bg-white/5 hover:text-white",
        )}
      >
        <Icon className="size-[18px]" />
        {label}
      </Link>
    );
  });
}

export function Sidebar() {
  return (
    <>
      <aside className="fixed inset-y-0 left-0 hidden w-72 flex-col bg-sidebar px-5 py-6 lg:flex">
        <Brand />
        <p className="mb-3 mt-10 px-3 text-[11px] font-semibold uppercase tracking-[0.2em] text-slate-500">
          Workspace
        </p>
        <nav aria-label="Primary navigation" className="space-y-1">
          <NavigationLinks />
        </nav>
        <div className="mt-auto rounded-2xl border border-emerald-400/10 bg-white/[0.04] p-4">
          <Badge className="border-emerald-400/20 bg-emerald-400/10 text-emerald-300">
            <Leaf className="size-3.5" />
            MVP foundation
          </Badge>
          <p className="mt-3 text-sm leading-6 text-slate-400">
            Deterministic intelligence built from verified air quality data.
          </p>
        </div>
      </aside>

      <div className="bg-sidebar px-4 pb-3 pt-4 lg:hidden">
        <Brand />
        <nav
          aria-label="Primary navigation"
          className="mt-4 flex gap-1 overflow-x-auto pb-1"
        >
          <NavigationLinks compact />
        </nav>
      </div>
    </>
  );
}
