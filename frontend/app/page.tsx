import Link from "next/link";
import {
  ArrowRight,
  BookOpen,
  ChartNoAxesColumn,
  Database,
  FileText,
  Megaphone,
  Sparkles,
  UsersRound,
} from "lucide-react";
import { Badge } from "@/components/ui/Badge";
import { buttonStyles } from "@/components/ui/Button";
import { Card, CardDescription, CardTitle } from "@/components/ui/Card";

const workflow = [
  {
    step: "01",
    title: "Prepare data",
    description:
      "Upload and clean city-level air quality records with transparent validation rules.",
  },
  {
    step: "02",
    title: "Study patterns",
    description:
      "Explore AQI trends, pollutant comparisons, anomaly flags, and city summaries.",
  },
  {
    step: "03",
    title: "Communicate findings",
    description:
      "Turn verified metrics into briefs, outreach drafts, public content, and reports.",
  },
];

const features = [
  {
    icon: Database,
    title: "Dataset readiness",
    description: "A traceable flow for uploaded, cleaned, and processed files.",
  },
  {
    icon: ChartNoAxesColumn,
    title: "AQI analysis",
    description: "Clear dashboard views grounded in actual computed values.",
  },
  {
    icon: BookOpen,
    title: "Research briefs",
    description: "Structured findings suitable for internal research review.",
  },
  {
    icon: Megaphone,
    title: "Content studio",
    description: "Evidence-based awareness content built from selected insights.",
  },
  {
    icon: UsersRound,
    title: "Stakeholder outreach",
    description: "Organized contacts and thoughtful communication drafts.",
  },
  {
    icon: FileText,
    title: "Exportable reports",
    description: "Markdown-first reporting with LaTeX support planned next.",
  },
];

export default function OverviewPage() {
  return (
    <div className="space-y-10">
      <section className="hero-grid overflow-hidden rounded-3xl border border-emerald-100 bg-white px-6 py-8 sm:px-9 sm:py-10 lg:px-12 lg:py-12">
        <div className="grid items-center gap-10 lg:grid-cols-[1.08fr_0.92fr]">
          <div>
            <Badge className="mb-6">
              <Sparkles className="size-3.5" />
              Climate-tech research workspace
            </Badge>
            <h1 className="max-w-3xl text-4xl font-semibold leading-tight tracking-tight text-slate-950 sm:text-5xl">
              Turn air quality data into credible climate action insights.
            </h1>
            <p className="mt-5 max-w-xl text-base leading-8 text-slate-600 sm:text-lg">
              AirLens brings Indian air quality analysis, research reporting, and
              stakeholder communication into one focused workspace.
            </p>
            <div className="mt-8 flex flex-col gap-3 sm:flex-row">
              <Link href="/datasets" className={buttonStyles()}>
                Explore datasets
                <ArrowRight className="size-4" />
              </Link>
              <Link
                href="/dashboard"
                className={buttonStyles({ variant: "secondary" })}
              >
                View dashboard
              </Link>
            </div>
          </div>

          <Card className="border-emerald-100 bg-white/90 p-5 sm:p-6">
            <div className="flex items-center justify-between border-b border-slate-100 pb-5">
              <div>
                <p className="text-xs font-medium uppercase tracking-[0.18em] text-slate-400">
                  Workspace pipeline
                </p>
                <p className="mt-2 font-semibold text-slate-900">
                  Research foundation
                </p>
              </div>
              <Badge>Ready to build</Badge>
            </div>
            <div className="space-y-3 pt-5">
              {["Dataset ingestion", "Analysis metrics", "Generated outputs"].map(
                (label, index) => (
                  <div
                    key={label}
                    className="flex items-center justify-between rounded-xl border border-slate-100 bg-slate-50 px-4 py-3.5"
                  >
                    <div className="flex items-center gap-3 text-sm font-medium text-slate-700">
                      <span className="flex size-7 items-center justify-center rounded-lg bg-emerald-100 text-xs font-semibold text-emerald-700">
                        {index + 1}
                      </span>
                      {label}
                    </div>
                    <span className="text-xs text-slate-400">Planned</span>
                  </div>
                ),
              )}
            </div>
          </Card>
        </div>
      </section>

      <section aria-labelledby="workflow-title" className="space-y-5">
        <div>
          <p className="text-sm font-medium text-emerald-700">Workflow</p>
          <h2
            id="workflow-title"
            className="mt-2 text-2xl font-semibold tracking-tight text-slate-950"
          >
            From raw observations to informed outreach
          </h2>
        </div>
        <div className="grid gap-5 md:grid-cols-3">
          {workflow.map(({ description, step, title }) => (
            <Card key={step} className="p-6">
              <span className="font-mono text-sm font-medium text-emerald-600">
                {step}
              </span>
              <CardTitle className="mt-5">{title}</CardTitle>
              <CardDescription className="mt-3">{description}</CardDescription>
            </Card>
          ))}
        </div>
      </section>

      <section aria-labelledby="features-title" className="space-y-5">
        <div className="flex flex-col justify-between gap-3 sm:flex-row sm:items-end">
          <div>
            <p className="text-sm font-medium text-emerald-700">Modules</p>
            <h2
              id="features-title"
              className="mt-2 text-2xl font-semibold tracking-tight text-slate-950"
            >
              A complete research and outreach toolkit
            </h2>
          </div>
          <p className="max-w-sm text-sm leading-6 text-slate-500">
            Functional capabilities arrive as real dataset workflows are built.
          </p>
        </div>
        <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
          {features.map(({ description, icon: Icon, title }) => (
            <Card key={title} className="group p-6">
              <span className="flex size-11 items-center justify-center rounded-xl bg-emerald-50 text-emerald-700 transition-colors group-hover:bg-emerald-100">
                <Icon className="size-5" />
              </span>
              <CardTitle className="mt-5">{title}</CardTitle>
              <CardDescription className="mt-3">{description}</CardDescription>
            </Card>
          ))}
        </div>
      </section>

      <section className="flex flex-col items-start justify-between gap-5 rounded-3xl bg-sidebar p-7 text-white sm:p-9 lg:flex-row lg:items-center">
        <div>
          <p className="text-sm font-medium text-emerald-300">Next milestone</p>
          <h2 className="mt-2 text-2xl font-semibold tracking-tight">
            Build the verified dataset pipeline.
          </h2>
          <p className="mt-3 max-w-xl text-sm leading-6 text-slate-300">
            Upload, validate, and clean city-level records before generating any
            analytical output.
          </p>
        </div>
        <Link
          href="/datasets"
          className={buttonStyles({
            className: "shrink-0 bg-emerald-500 hover:bg-emerald-400",
          })}
        >
          Open datasets
          <ArrowRight className="size-4" />
        </Link>
      </section>
    </div>
  );
}
