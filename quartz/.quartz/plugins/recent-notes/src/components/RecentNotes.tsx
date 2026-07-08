import type { QuartzComponent, QuartzComponentProps } from "@quartz-community/types";
import { classNames } from "../util/lang";
import { i18n } from "../i18n";
import { resolveRelative } from "../util/path";
import { getDate, formatDate } from "../util/date";
import { byDateAndAlphabetical } from "../util/sort";
import style from "./styles/recentNotes.scss";

type QuartzComponentConstructor<Options extends object | undefined = undefined> = (
  opts: Options,
) => QuartzComponent;

interface QuartzPluginData {
  slug?: string;
  filePath?: string;
  dates?: Record<string, Date>;
  frontmatter?: {
    title?: string;
    tags?: string[];
    [key: string]: unknown;
  };
  [key: string]: unknown;
}

interface GlobalConfiguration {
  locale: string;
  defaultDateType: string;
  [key: string]: unknown;
}

export interface RecentNotesOptions {
  title?: string;
  limit: number;
  linkToMore: string | false;
  showTags: boolean;
  filter: (f: QuartzPluginData) => boolean;
  sort: (f1: QuartzPluginData, f2: QuartzPluginData) => number;
}

const defaultOptions = (cfg: GlobalConfiguration): RecentNotesOptions => ({
  limit: 3,
  linkToMore: false,
  showTags: true,
  filter: () => true,
  sort: byDateAndAlphabetical(cfg),
});

export default ((userOpts?: Partial<RecentNotesOptions>) => {
  const RecentNotes: QuartzComponent = ({
    allFiles,
    fileData,
    displayClass,
    cfg,
  }: QuartzComponentProps & { displayClass?: string }) => {
    const globalCfg = cfg as unknown as GlobalConfiguration;
    const opts = { ...defaultOptions(globalCfg), ...userOpts };
    const pages = (allFiles as QuartzPluginData[]).filter(opts.filter).sort(opts.sort);
    const remaining = Math.max(0, pages.length - opts.limit);
    const slug = fileData.slug as string | undefined;
    const locale = cfg.locale ?? "en-US";
    return (
      <div class={classNames(displayClass, "recent-notes")}>
        <h3>{opts.title ?? i18n(locale).components.recentNotes.title}</h3>
        <ul class="recent-ul">
          {pages.slice(0, opts.limit).map((page) => {
            const title = page.frontmatter?.title ?? "Untitled";
            const tags = page.frontmatter?.tags ?? [];

            return (
              <li class="recent-li">
                <div class="section">
                  <div class="desc">
                    <h3>
                      <a href={resolveRelative(slug!, page.slug!)} class="internal">
                        {title}
                      </a>
                    </h3>
                  </div>
                  {page.dates && (
                    <p class="meta">
                      <time datetime={getDate(globalCfg, page)?.toISOString()}>
                        {formatDate(getDate(globalCfg, page)!, locale)}
                      </time>
                    </p>
                  )}
                  {opts.showTags && (
                    <ul class="tags">
                      {tags.map((tag) => (
                        <li>
                          <a class="internal tag-link" href={resolveRelative(slug!, `tags/${tag}`)}>
                            {tag}
                          </a>
                        </li>
                      ))}
                    </ul>
                  )}
                </div>
              </li>
            );
          })}
        </ul>
        {opts.linkToMore && remaining > 0 && (
          <p>
            <a href={resolveRelative(slug!, opts.linkToMore)}>
              {i18n(locale).components.recentNotes.seeRemainingMore({ remaining })}
            </a>
          </p>
        )}
      </div>
    );
  };

  RecentNotes.css = style;
  return RecentNotes;
}) satisfies QuartzComponentConstructor;
