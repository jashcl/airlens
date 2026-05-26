import {
  ModulePlaceholder,
  PageHeader,
} from "@/components/layout/PageShell";
import {
  Card,
  CardDescription,
  CardTitle,
} from "@/components/ui/Card";
import type { ModuleOverview } from "@/lib/types";

const moduleOverview: ModuleOverview = {
  label: "Analytics",
  title: "AQI dashboard",
  description:
    "A decision-ready view of trends, pollutants, cities, and unusual air quality events.",
  purpose:
    "Once cleaned data is available, this dashboard will present measured AQI summaries and pollutant patterns without inventing missing figures.",
  capabilities: [
    "Compare city AQI summaries and pollutant profiles.",
    "Explore AQI trend and bucket distribution views.",
    "Surface worst pollution days and simple anomaly flags.",
  ],
};

const metrics = ["Average AQI", "Cities analyzed", "Anomalies detected"];

export default function DashboardPage() {
  return (
    <>
      <PageHeader {...moduleOverview} />
      <div className="mb-5 grid gap-4 md:grid-cols-3">
        {metrics.map((metric) => (
          <Card key={metric} className="p-5">
            <CardDescription>{metric}</CardDescription>
            <CardTitle className="mt-4 text-3xl text-slate-300">--</CardTitle>
            <p className="mt-2 text-xs text-slate-400">Awaiting cleaned dataset</p>
          </Card>
        ))}
      </div>
      <ModulePlaceholder {...moduleOverview} />
    </>
  );
}
