export type ModuleStatus = "Planned" | "Foundation ready";

export interface NavigationItem {
  href: string;
  label: string;
}

export interface ModuleOverview {
  label: string;
  title: string;
  description: string;
  purpose: string;
  capabilities: string[];
  status?: ModuleStatus;
}
