export function cn(...classes: Array<string | false | undefined | null>) { return classes.filter(Boolean).join(" "); }
export function fmt(n: number | null | undefined) { return n === null || n === undefined ? "—" : Number(n).toLocaleString(); }
