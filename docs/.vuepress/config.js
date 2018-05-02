module.exports = {
  title: 'PreProgramming 2017',
  description: 'PreProgramming for IT15 students',
  base: '/PreProgramming-60/',

  themeConfig: {

    // GitHub edit link
    repo: 'sagelga/PreProgramming-60',
    repoLabel: 'Repository',
    docsRepo: 'sagelga/PreProgramming-60',
    docsDir: 'docs',
    editLinks: true,
    editLinkText: 'Help us improve this page!',

    // Sidebar
    sidebar: [
      {
        title: 'Python Lesson',
        collapsable: true,
        children: [
          '/Lecture Cheat Sheet/Week 1 - IO.md',
          '/Lecture Cheat Sheet/Week 2 - Functions.md',
          '/Lecture Cheat Sheet/Week 3 - Math Library.md',
          '/Lecture Cheat Sheet/Week 4 - Strings.md',
          '/Lecture Cheat Sheet/Week 5 - Condition.md',
          '/Lecture Cheat Sheet/Week 6 - Loops.md',
          '/Lecture Cheat Sheet/Week 7 - Lists + Tuples.md',
          '/Lecture Cheat Sheet/Week 8 - Dictionary.md',
          '/Lecture Cheat Sheet/Week 9 - Recursion.md'
        ]
      },
    ],

    // Navigation Bar
    nav: [
      { text: '🏠 Home', link: '/' },
    ],

    // Search bar
    searchMaxSuggestions: 20
  }
}
