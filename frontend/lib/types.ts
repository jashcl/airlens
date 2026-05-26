export type UploadResponse = {
  filename: string; original_rows: number; cleaned_rows: number; duplicate_rows_removed: number;
  columns: string[]; missing_values_before: Record<string, number>; missing_values_after: Record<string, number>;
  detected_cities: string[]; detected_pollutants: string[]; min_date: string; max_date: string;
  preview_rows: Record<string, string | number | null>[];
};
export type CitySummary = { city:string; total_records:number; min_date:string; max_date:string; average_aqi:number; max_aqi:number; min_aqi:number; dominant_aqi_bucket:string; average_pm25?:number|null; average_pm10?:number|null; worst_day:{date:string;aqi:number}; best_day:{date:string;aqi:number}; available_pollutants:string[] };
export type TrendPoint = Record<string, string | number | null>;
export type Stakeholder = { id?:number; name:string; organization:string; organization_type:string; city?:string; email?:string; phone_or_linkedin?:string; interest_area?:string; status:string; notes?:string; last_contacted?:string; next_followup?:string; draft_message?:string; created_at?:string; updated_at?:string };
export type ResearchLog = { id?:number; title:string; topic?:string; source_name?:string; source_url?:string; summary?:string; tags?:string; status:string; created_at?:string; updated_at?:string };
