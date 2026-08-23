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
      disable404Route: true,
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
          label: '今日',
          items: [
            { label: '首页看板', slug: '' },
            { label: '待评审', link: '/reviews/' },
            { label: '投研驾驶舱', link: '/dashboard/h1-2-storage/' },
          ],
        },
        {
          label: '价投框架',
          items: [{ label: '价值投资框架', slug: 'investing/value-framework' }],
        },
        ...generatedSidebar,
      ],
    }),
  ],
});
