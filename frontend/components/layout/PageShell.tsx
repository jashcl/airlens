import type { ReactNode } from "react";
import { CheckCircle2 } from "lucide-react";
import { Sidebar } from "@/components/layout/Sidebar";
import { Topbar } from "@/components/layout/Topbar";
import { Badge } from "@/components/ui/Badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/Card";
import type { ModuleOverview } from "@/lib/types";

export function PageShell({ children }: { children: ReactNode }) {
  return (
    <div className="min-h-screen bg-[#f6f8f5] text-slate-900">
      <Sidebar />
      <div className="min-h-screen min-w-0 bg-[#f6f8f5] lg:pl-72">
        <Topbar />
        <main className="mx-auto max-w-7xl px-4 py-7 sm:px-6 lg:px-10 lg:py-9">
          {children}
        </main>
      </div>
    </div>
  );
}

interface PageHeaderProps {
  action?: ReactNode;
  description: string;
  label: string;
  status?: ModuleOverview["status"];
  title: string;
}

export function PageHeader({
  action,
  description,
  label,
  status = "Planned",
  title,
}: PageHeaderProps) {
  return (
    <header className="mb-8 flex flex-col justify-between gap-5 md:flex-row md:items-end">
      <div className="max-w-3xl space-y-4">
        <div className="flex flex-wrap items-center gap-3">
          <Badge>{label}</Badge>
          <Badge variant="outline">{status}</Badge>
        </div>
        <h1 className="text-3xl font-semibold tracking-tight text-slate-950 sm:text-4xl">
          {title}
        </h1>
        <p className="text-base leading-7 text-slate-600">{description}</p>
      </div>
      {action}
    </header>
  );
}

export function ModulePlaceholder({
  capabilities,
  purpose,
}: Pick<ModuleOverview, "capabilities" | "purpose">) {
  return (
    <section className="grid gap-5 lg:grid-cols-[1.12fr_0.88fr]">
      <Card className="flex min-h-64 flex-col justify-between">
        <CardHeader>
          <Badge variant="neutral">Page purpose</Badge>
          <CardTitle className="mt-5 text-2xl">Built for meaningful evidence</CardTitle>
          <CardDescription className="max-w-xl text-base leading-7">
            {purpose}
          </CardDescription>
        </CardHeader>
        <CardContent>
          <p className="rounded-xl border border-emerald-100 bg-emerald-50 px-4 py-3 text-sm text-emerald-900">
            Real metrics will appear here once the dataset workflow is implemented.
          </p>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Planned capabilities</CardTitle>
          <CardDescription>
            The first functional release of this module will support:
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          {capabilities.map((capability) => (
            <div key={capability} className="flex gap-3">
              <CheckCircle2 className="mt-0.5 size-4 shrink-0 text-emerald-600" />
              <span className="leading-6">{capability}</span>
            </div>
          ))}
        </CardContent>
      </Card>
    </section>
  );
}
