import { getDate } from "./date";

interface GlobalConfiguration {
  defaultDateType: string;
  [key: string]: unknown;
}

interface QuartzPluginData {
  dates?: Record<string, Date>;
  frontmatter?: {
    title?: string;
    [key: string]: unknown;
  };
  [key: string]: unknown;
}

export type SortFn = (f1: QuartzPluginData, f2: QuartzPluginData) => number;

export function byDateAndAlphabetical(cfg: GlobalConfiguration): SortFn {
  return (f1, f2) => {
    if (f1.dates && f2.dates) {
      return getDate(cfg, f2)!.getTime() - getDate(cfg, f1)!.getTime();
    } else if (f1.dates && !f2.dates) {
      return -1;
    } else if (!f1.dates && f2.dates) {
      return 1;
    }

    const f1Title = f1.frontmatter?.title?.toLowerCase() ?? "";
    const f2Title = f2.frontmatter?.title?.toLowerCase() ?? "";
    return f1Title.localeCompare(f2Title);
  };
}
