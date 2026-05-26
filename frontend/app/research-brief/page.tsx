import {
  ModulePlaceholder,
  PageHeader,
} from "@/components/layout/PageShell";
import type { ModuleOverview } from "@/lib/types";

const moduleOverview: ModuleOverview = {
  label: "Research output",
  title: "Research brief",
  description:
    "Translate measured air quality findings into a concise, defensible narrative.",
  purpose:
    "The research brief module will organize actual dashboard findings into structured context, methodology, key observations, and implications.",
  capabilities: [
    "Select computed metrics to support written findings.",
    "Generate a clear brief outline from verified analysis.",
    "Preserve data context and methodological notes.",
  ],
};

export default function ResearchBriefPage() {
  return (
    <>
      <PageHeader {...moduleOverview} />
      <ModulePlaceholder {...moduleOverview} />
    </>
  );
}
