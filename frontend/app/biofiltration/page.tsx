import {
  ModulePlaceholder,
  PageHeader,
} from "@/components/layout/PageShell";
import type { ModuleOverview } from "@/lib/types";

const moduleOverview: ModuleOverview = {
  label: "Intervention notes",
  title: "Biofiltration observations",
  description:
    "Document before-and-after environmental observations for intervention research.",
  purpose:
    "This is a software documentation module for comparing recorded observations around biofiltration or related interventions, not a hardware control system.",
  capabilities: [
    "Record intervention context and observation periods.",
    "Compare before-and-after measured observations.",
    "Capture cautious interpretation notes for review.",
  ],
};

export default function BiofiltrationPage() {
  return (
    <>
      <PageHeader {...moduleOverview} />
      <ModulePlaceholder {...moduleOverview} />
    </>
  );
}
