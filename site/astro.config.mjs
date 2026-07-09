import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import rosePine from 'starlight-theme-rose-pine';

export default defineConfig({
  site: 'https://annettehub.github.io',
  base: '/ai-investing',
  integrations: [
    starlight({
      title: 'AI Investing',
      description: 'Annette 的 AI 投研知识库',
      logo: {
        src: './src/assets/logo.svg',
        alt: 'AI Investing',
      },
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/Annettehub/ai-investing',
        },
      ],
      customCss: ['./src/styles/custom.css'],
      plugins: [
        rosePine({
          dark: { flavor: 'main', accent: 'foam' },
          light: { flavor: 'dawn', accent: 'pine' },
        }),
      ],
      sidebar: [
        {
          label: '开始',
          items: [
            { label: '首页', slug: '' },
            { label: '知识地图', slug: 'ai-map' },
          ],
        },
        {
          label: 'AI 投研',
          items: [
            { label: 'GPU vs ASIC', slug: 'concepts/gpu-asic' },
            { label: 'CPO 光互联', slug: 'concepts/cpo' },
            { label: 'AI 服务器供应链', slug: 'concepts/ai-server' },
            { label: '算力资本开支', slug: 'concepts/ai-capex' },
          ],
        },
        {
          label: '投资框架',
          items: [{ label: '价值投资框架', slug: 'investing/value-framework' }],
        },
        {
          label: '内容管线',
          items: [
            { label: '原始资料库', slug: 'pipeline/raw-sources' },
            { label: '自动同步', slug: 'pipeline/automation' },
          ],
        },
        {
          label: '02-kb 知识库',
          items: [
            { label: '总索引', slug: 'kb' },
            { label: '公司与标的', autogenerate: { directory: 'kb/entities', collapsed: true }, collapsed: true },
            { label: '概念框架', autogenerate: { directory: 'kb/concepts', collapsed: true }, collapsed: true },
            { label: '投资假设', autogenerate: { directory: 'kb/hypotheses', collapsed: true }, collapsed: true },
            { label: '来源摘要', autogenerate: { directory: 'kb/sources', collapsed: true }, collapsed: true },
          ],
        },
        {
          label: '04-output 输出',
          items: [
            { label: '输出总览', slug: 'outputs' },
            { label: '研究报告', autogenerate: { directory: 'outputs/research', collapsed: true }, collapsed: true },
            { label: '每日跟踪', autogenerate: { directory: 'outputs/today', collapsed: true }, collapsed: true },
            { label: '周度复盘', autogenerate: { directory: 'outputs/weekly', collapsed: true }, collapsed: true },
          ],
        },
      ],
    }),
  ],
});
