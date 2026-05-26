import { Bell, Search, Sparkles } from "lucide-react";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";

export function Topbar() {
  return (
    <header className="sticky top-0 z-10 flex h-20 items-center gap-4 border-b border-slate-200/90 bg-white/95 px-4 shadow-sm shadow-slate-900/[0.02] backdrop-blur sm:px-6 lg:px-10">
      <div className="min-w-0 flex-1">
        <p className="hidden text-xs font-medium uppercase tracking-[0.2em] text-slate-500 sm:block">
          Research workspace
        </p>
        <p className="truncate text-sm font-semibold text-slate-900 sm:mt-1">
          Indian Air Quality Intelligence
        </p>
      </div>

      <label className="relative hidden w-full max-w-xs md:block">
        <span className="sr-only">Search workspace</span>
        <Search className="absolute left-3.5 top-1/2 size-4 -translate-y-1/2 text-slate-500" />
        <Input
          aria-label="Search workspace"
          className="bg-slate-50 pl-10"
          placeholder="Search workspace"
          disabled
        />
      </label>

      <Badge variant="outline" className="hidden sm:inline-flex">
        <Sparkles className="size-3.5 text-emerald-600" />
        MVP build
      </Badge>

      <Button
        aria-label="Notifications will be available in a later phase"
        disabled
        size="icon"
        variant="ghost"
      >
        <Bell className="size-5" />
      </Button>
    </header>
  );
}
