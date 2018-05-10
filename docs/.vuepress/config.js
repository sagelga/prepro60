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
                collapsable: false,
                children: [
                    ['/Python/', 'Introduction'],
                    '/Python/IO.md',
                    '/Python/Operator.md',
                    '/Python/Strings.md',
                    '/Python/Functions.md',
                    '/Python/Condition.md',
                    '/Python/Loops.md',
                    '/Python/ListAndTuples.md',
                    '/Python/Dictionary.md',
                    '/Python/Recursion.md',
                    '/Python/PyLint.md',
                    '/Python/Built-In-Method.md',
                    '/Python/Built-In-Functions.md',
                    '/Python/MathLibrary.md',
                    '/Python/TryAndExcept.md',
                    '/Python/OOP.md',
                    '/Python/FileManipulate.md',
                ]
            },

            {
                title: 'Practice',
                collapsable: true,
                children: [
                  '/Online-Question/Week 1/',
                  '/Online-Question/Week 2/',
                  '/Online-Question/Week 3/',
                  '/Online-Question/Week 4/',
                  '/Online-Question/Week 5/',
                  '/Online-Question/Week 6/'
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
