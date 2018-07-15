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
        repoLabel: 'PrePro60 Repo',
        docsRepo: 'sagelga/PreProgramming-60',
        docsDir: 'docs',
        editLinks: true,
        editLinkText: '✏️ Edit',

        lastUpdated: '🕑',

        // Navigation Bar
        nav: [
            { text: 'Python Cheatsheet', link: 'https://sagelga.github.io/cheatsheet/#/Python/' },
            { text: 'Report a Problem', link: 'https://github.com/sagelga/PreProgramming-60/issues' }

        ],

        // Sidebar
        sidebar: [
            {
                title: 'Online Question',
                collapsable: true,
                children: [
                    'Online-Question/Week1/Special-ITCAMP13.md',	
                    'Online-Question/Week1/Absolute.md',
                    'Online-Question/Week1/Discounted.md',
                    'Online-Question/Week1/Distance.md',
                    'Online-Question/Week1/Echo.md',
                    'Online-Question/Week1/FirstImpression.md',
                    'Online-Question/Week1/IO.md',
                    'Online-Question/Week1/MathematicianV2.md',
                    'Online-Question/Week1/Mathematician.md',
                    'Online-Question/Week1/MaxMeanMin.md',
                    'Online-Question/Week1/PersonalInformation.md',
                    'Online-Question/Week1/SecretCode.md',
                    'Online-Question/Week1/SquareRoot.md',
                    'Online-Question/Week1/ToInteger.md',
                    'Online-Question/Week1/TooManyLines.md',
                    'Online-Question/Week1/GroupUpWithMe.md',
                    'Online-Question/Week1/Hardcore-BankNotes.md',
                    'Online-Question/Week1/Hardcore-Correlated.md',
                    'Online-Question/Week1/Hardcore-CramersRule.md',
                    'Online-Question/Week1/Hardcore-EQUALLYDistributed.md',
                    'Online-Question/Week1/Hardcore-Grading.md',
                    'Online-Question/Week1/Hardcore-Sequence.md',
                    'Online-Question/Week1/Hardcore-TaxNotIncluded.md',
                    'Online-Question/Week1/Hardcore-WeirdThatsOdd.md'
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
