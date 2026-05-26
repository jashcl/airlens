import {
  ModulePlaceholder,
  PageHeader,
} from "@/components/layout/PageShell";
import type { ModuleOverview } from "@/lib/types";

const moduleOverview: ModuleOverview = {
  label: "Public engagement",
  title: "Content studio",
  description:
    "Shape reliable analysis into audience-appropriate climate awareness content.",
  purpose:
    "This studio will use deterministic templates and selected computed metrics to draft public notes, blog material, and professional social posts.",
  capabilities: [
    "Choose an insight and a communication format.",
    "Draft content using only available evidence.",
    "Review messaging before publishing outside AirLens.",
  ],
};

export default function ContentStudioPage() {
  return (
    <>
      <PageHeader {...moduleOverview} />
      <ModulePlaceholder {...moduleOverview} />
    </>
  );
}
