module.exports = {
    title: 'PreProgramming 2016',
    description: 'PreProgramming for PSIT Students',
    base: '/PreProgramming-60/',

    markdown: {
        lineNumbers: true,
    },

    themeConfig: {

        // GitHub edit link
        repo: 'sagelga/PreProgramming-60',
        repoLabel: 'PrePro60 Repository',
        docsRepo: 'sagelga/PreProgramming-60',
        docsDir: 'docs',
        editLinks: true,
        editLinkText: '✏️ Edit',

        lastUpdated: '🕑',

        // Navigation Bar
        nav: [
            { text: 'Report a Problem', link: 'https://github.com/sagelga/PreProgramming-60/issues' },
        ],

        // Sidebar
        sidebar: [
            {
                title: 'Lecture Cheatsheet',
                collapsable: false,
                children: [
                  '/cheatsheet/Introduction/',
                    '/cheatsheet/IO/',
                    '/cheatsheet/Function/',
                    '/cheatsheet/String/',
                    '/cheatsheet/Loop/',
                    '/cheatsheet/Condition/',
                    '/cheatsheet/List/',
                    '/cheatsheet/Dictionary/',
                ]
            },

            {
                title: 'Python Law',
                collapsable: false,
                children: [
                    '/cheatsheet/PyLint/',
                    '/cheatsheet/BuildInFunctions/',
                    '/cheatsheet/BuildInMethod/',
                    '/cheatsheet/MathLibrary/',
                ]
            }
        ],

        // Search bar
        searchMaxSuggestions: 20
    }
}
