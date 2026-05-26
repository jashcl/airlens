const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8000";
async function req<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, { ...options, headers: { ...(options?.headers || {}) } });
  if (!res.ok) {
    let msg = `Request failed: ${res.status}`;
    try { const data = await res.json(); msg = data.detail || msg; } catch {}
    throw new Error(typeof msg === "string" ? msg : JSON.stringify(msg));
  }
  const contentType = res.headers.get("content-type") || "";
  if (contentType.includes("application/json")) return res.json();
  return res.text() as Promise<T>;
}
export async function uploadCsv(file: File) { const form = new FormData(); form.append("file", file); return req<any>("/datasets/upload", { method: "POST", body: form }); }
export const getCities = async () => (await req<{cities:string[]}>("/analysis/cities")).cities;
export const getSummary = (city:string) => req<any>(`/analysis/summary/${encodeURIComponent(city)}`);
export const getAqiTrend = (city:string) => req<any[]>(`/analysis/aqi-trend/${encodeURIComponent(city)}`);
export const getPmTrend = (city:string) => req<any[]>(`/analysis/pm25-pm10/${encodeURIComponent(city)}`);
export const getPollutantComparison = (city:string) => req<any[]>(`/analysis/pollutant-comparison/${encodeURIComponent(city)}`);
export const getBuckets = (city:string) => req<any[]>(`/analysis/aqi-buckets/${encodeURIComponent(city)}`);
export const getWorstDays = (city:string) => req<any[]>(`/analysis/worst-days/${encodeURIComponent(city)}`);
export const getAnomalies = (city:string) => req<any>(`/analysis/anomalies/${encodeURIComponent(city)}`);
export const generateBrief = (city:string, audience:string) => req<any>("/reports/research-brief", { method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify({city,audience}) });
export const downloadMarkdown = (city:string) => req<string>(`/reports/${encodeURIComponent(city)}/markdown`);
export const downloadLatex = (city:string) => req<string>(`/reports/${encodeURIComponent(city)}/latex`);
export const generateContent = (type:string, city:string, audience:string, tone:string) => req<any>(`/content/${type}`, { method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify({city,audience,tone}) });
export const listStakeholders = () => req<any[]>("/outreach/stakeholders");
export const createStakeholder = (data:any) => req<any>("/outreach/stakeholders", { method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(data) });
export const deleteStakeholder = (id:number) => req<any>(`/outreach/stakeholders/${id}`, { method:"DELETE" });
export const generateEmail = (id:number, city:string) => req<any>(`/outreach/stakeholders/${id}/generate-email`, { method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify({city}) });
export const listResearchLogs = () => req<any[]>("/research-log");
export const createResearchLog = (data:any) => req<any>("/research-log", { method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(data) });
export const deleteResearchLog = (id:number) => req<any>(`/research-log/${id}`, { method:"DELETE" });
export const bioCompare = (data:any) => req<any>("/biofiltration/compare", { method:"POST", headers:{"Content-Type":"application/json"}, body:JSON.stringify(data) });
export const bioRecords = () => req<any[]>("/biofiltration/records");
export function downloadText(filename:string, content:string){ const blob=new Blob([content],{type:"text/plain;charset=utf-8"}); const url=URL.createObjectURL(blob); const a=document.createElement("a"); a.href=url; a.download=filename; a.click(); URL.revokeObjectURL(url); }
