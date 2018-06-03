module.exports = {
    title: 'PreProgramming 2016',
    description: 'PreProgramming for PSIT Students',
    base: '/PreProgramming-60/',

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
                    '/Lecture Cheat Sheet/IO.md',
                    '/Lecture Cheat Sheet/Functions.md',
                    '/Lecture Cheat Sheet/Strings.md',
                    '/Lecture Cheat Sheet/Loops.md',
                    '/Lecture Cheat Sheet/Condition.md',
                    '/Lecture Cheat Sheet/ListsAndTuples.md',
                    '/Lecture Cheat Sheet/Dictionary.md',
                ]
            },

            {
                title: 'Python Law',
                collapsable: false,
                children: [
                    '/Lecture Cheat Sheet/Rule/PyLint.md',
                    '/Lecture Cheat Sheet/Rule/BuildInFunctions.md',
                    '/Lecture Cheat Sheet/Rule/BuildInMethod.md',
                    '/Lecture Cheat Sheet/Rule/MathLibrary.md',
                ]
            }
        ],

        // Search bar
        searchMaxSuggestions: 20
    }
}
