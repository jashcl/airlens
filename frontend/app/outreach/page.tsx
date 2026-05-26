import {
  ModulePlaceholder,
  PageHeader,
} from "@/components/layout/PageShell";
import type { ModuleOverview } from "@/lib/types";

const moduleOverview: ModuleOverview = {
  label: "Stakeholders",
  title: "Outreach CRM",
  description:
    "Organize relevant stakeholders and prepare evidence-led outreach drafts.",
  purpose:
    "The outreach workspace will track stakeholder context, contact status, and communication drafts grounded in approved research findings.",
  capabilities: [
    "Record stakeholder organizations and engagement context.",
    "Prepare email drafts linked to research insights.",
    "Track follow-up status without sending messages automatically.",
  ],
};

export default function OutreachPage() {
  return (
    <>
      <PageHeader {...moduleOverview} />
      <ModulePlaceholder {...moduleOverview} />
    </>
  );
}
