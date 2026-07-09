import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import rosePine from 'starlight-theme-rose-pine';
import generatedSidebar from './sidebar.generated.mjs';

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
      components: {
        Sidebar: './src/components/Sidebar.astro',
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
        ...generatedSidebar,
      ],
    }),
  ],
});
