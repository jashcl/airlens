import {
  ModulePlaceholder,
  PageHeader,
} from "@/components/layout/PageShell";
import type { ModuleOverview } from "@/lib/types";

const moduleOverview: ModuleOverview = {
  label: "Documentation",
  title: "Research log",
  description:
    "Maintain a practical record of sources, observations, decisions, and drafts.",
  purpose:
    "This log will make research activity traceable by recording what was explored, which source supported it, and the status of resulting work.",
  capabilities: [
    "Capture research notes, sources, and tags.",
    "Record activity dates and draft status.",
    "Link evidence gathering to later communication outputs.",
  ],
};

export default function ResearchLogPage() {
  return (
    <>
      <PageHeader {...moduleOverview} />
      <ModulePlaceholder {...moduleOverview} />
    </>
  );
}
