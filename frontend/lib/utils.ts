export function cn(
  ...classes: Array<string | false | null | undefined>
): string {
  return classes
    .filter((className): className is string => Boolean(className))
    .join(" ");
}
