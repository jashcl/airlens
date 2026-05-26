import { Upload } from "lucide-react";
import {
  ModulePlaceholder,
  PageHeader,
} from "@/components/layout/PageShell";
import { Button } from "@/components/ui/Button";
import type { ModuleOverview } from "@/lib/types";

const moduleOverview: ModuleOverview = {
  label: "Data readiness",
  title: "Datasets",
  description:
    "Prepare trustworthy city-level air quality files for every downstream insight.",
  purpose:
    "This workspace will manage CSV uploads, required-column checks, cleaning summaries, and the latest processed dataset used for analysis.",
  capabilities: [
    "Upload the primary city_day.csv dataset.",
    "Validate City, Date, and AQI before processing.",
    "Track missing values and cleaning outcomes clearly.",
  ],
};

export default function DatasetsPage() {
  return (
    <>
      <PageHeader
        {...moduleOverview}
        action={
          <Button disabled>
            <Upload className="size-4" />
            Upload dataset
          </Button>
        }
      />
      <ModulePlaceholder {...moduleOverview} />
    </>
  );
}
