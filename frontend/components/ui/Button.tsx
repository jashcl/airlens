import type { ButtonHTMLAttributes } from "react";
import { cn } from "@/lib/utils";

export type ButtonVariant = "primary" | "secondary" | "ghost";
export type ButtonSize = "default" | "sm" | "icon";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  size?: ButtonSize;
}

const variants: Record<ButtonVariant, string> = {
  primary:
    "bg-emerald-700 text-white shadow-sm shadow-emerald-900/10 hover:bg-emerald-800",
  secondary:
    "border border-slate-200 bg-white text-slate-800 hover:border-emerald-200 hover:bg-emerald-50",
  ghost: "text-slate-700 hover:bg-slate-100 hover:text-slate-950",
};

const sizes: Record<ButtonSize, string> = {
  default: "h-11 px-5",
  sm: "h-9 px-4",
  icon: "size-10",
};

export function buttonStyles({
  className,
  size = "default",
  variant = "primary",
}: {
  className?: string;
  size?: ButtonSize;
  variant?: ButtonVariant;
} = {}) {
  return cn(
    "inline-flex items-center justify-center gap-2 rounded-xl text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-emerald-600 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:border-slate-200 disabled:bg-slate-100 disabled:text-slate-600 disabled:shadow-none",
    variants[variant],
    sizes[size],
    className,
  );
}

export function Button({
  className,
  size = "default",
  variant = "primary",
  type = "button",
  ...props
}: ButtonProps) {
  return (
    <button
      className={buttonStyles({ className, size, variant })}
      type={type}
      {...props}
    />
  );
}
