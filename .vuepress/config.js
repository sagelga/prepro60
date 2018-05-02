module.exports = {
  title: 'Hello VuePress',
  description: 'Just playing around'

  base: "/PreProgramming-60/"

  configureWebpack: {
    resolve: {
      alias: {
        '@home': 'img'
      }
    }
  }

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Guide', link: '/guide/' },
      { text: 'External', link: 'https://google.com' },
    ]
  }
}
