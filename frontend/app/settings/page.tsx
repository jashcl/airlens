import {
  ModulePlaceholder,
  PageHeader,
} from "@/components/layout/PageShell";
import { Badge } from "@/components/ui/Badge";
import {
  Card,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/Card";
import { Input } from "@/components/ui/Input";
import { API_BASE_URL } from "@/lib/api";
import type { ModuleOverview } from "@/lib/types";

const moduleOverview: ModuleOverview = {
  label: "Configuration",
  title: "Settings",
  description:
    "Review workspace configuration and planned integration preferences.",
  purpose:
    "Settings will provide simple application configuration for local development and report defaults as the platform features become available.",
  capabilities: [
    "Review the configured API base address.",
    "Control future report and workspace preferences.",
    "Keep MVP setup straightforward and transparent.",
  ],
};

export default function SettingsPage() {
  return (
    <>
      <PageHeader {...moduleOverview} />
      <Card className="mb-5">
        <CardHeader className="flex flex-col justify-between gap-3 sm:flex-row sm:items-start">
          <div>
            <CardTitle>Backend endpoint</CardTitle>
            <CardDescription className="mt-2">
              Stored for future integration. No requests are made from this scaffold.
            </CardDescription>
          </div>
          <Badge variant="outline">Not connected</Badge>
        </CardHeader>
        <Input aria-label="API base URL" readOnly value={API_BASE_URL} />
      </Card>
      <ModulePlaceholder {...moduleOverview} />
    </>
  );
}
