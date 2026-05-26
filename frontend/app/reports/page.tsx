import { FileText } from "lucide-react";
import {
  ModulePlaceholder,
  PageHeader,
} from "@/components/layout/PageShell";
import { Button } from "@/components/ui/Button";
import type { ModuleOverview } from "@/lib/types";

const moduleOverview: ModuleOverview = {
  label: "Exports",
  title: "Reports",
  description:
    "Assemble transparent, shareable documentation from selected AirLens outputs.",
  purpose:
    "Reporting will combine actual dataset summaries, analysis findings, and approved narrative sections into reproducible Markdown-first exports.",
  capabilities: [
    "Generate Markdown research reports first.",
    "Prepare LaTeX export after report structure is validated.",
    "Keep analysis outputs traceable to real source metrics.",
  ],
};

export default function ReportsPage() {
  return (
    <>
      <PageHeader
        {...moduleOverview}
        action={
          <Button disabled variant="secondary">
            <FileText className="size-4" />
            New report
          </Button>
        }
      />
      <ModulePlaceholder {...moduleOverview} />
    </>
  );
}
