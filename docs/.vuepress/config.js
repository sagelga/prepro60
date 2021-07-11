module.exports = {
    title: 'PreProgramming 2016',
    description: 'PreProgramming for PSIT Students',
    base: '/',

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
        nav: [{
                text: 'Python Cheatsheet',
                link: 'https://learn.sagelga.com/python/'
            },
            {
                text: 'Report a Problem',
                link: 'https://github.com/sagelga/PreProgramming-60/issues'
            }

        ],

        // Sidebar
        sidebar: [{
                title: 'Online Question',
                collapsable: true,
                children: [
                    // Week 1
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
                    'Online-Question/Week1/Hardcore-WeirdThatsOdd.md',
                    // Week 2
                    'Online-Question/Week2/Base2Average.md',
                    'Online-Question/Week2/Congratulations.md',
                    'Online-Question/Week2/Docstring.md',
                    'Online-Question/Week2/InitialD1.md',
                    'Online-Question/Week2/McDonalds.md',
                    'Online-Question/Week2/NumericalDigit.md',
                    'Online-Question/Week2/SayHo.md',
                    'Online-Question/Week2/SqOf3.md',
                    'Online-Question/Week2/TheVeryBest.md',
                    'Online-Question/Week2/Thermometer.md',
                    'Online-Question/Week2/TimeConverter.md',
                    'Online-Question/Week2/VATWithServiceCharge.md',
                    // Week 3
                    'Online-Question/Week3/AccessCharacter.md',
                    'Online-Question/Week3/BinaryDecoder.md',
                    'Online-Question/Week3/BinaryEncoder.md',
                    'Online-Question/Week3/CaesarCypher.md',
                    'Online-Question/Week3/Card.md',
                    'Online-Question/Week3/EarthIsCenterUniverse.md',
                    'Online-Question/Week3/EarthIsCenterUniverse2.md',
                    'Online-Question/Week3/ExpensiveVovel.md',
                    'Online-Question/Week3/Hello.md',
                    'Online-Question/Week3/MuliplePrint.md',
                    'Online-Question/Week3/Palindrome.md',
                    'Online-Question/Week3/PlusString.md',
                    'Online-Question/Week3/STIC.md',
                    'Online-Question/Week3/SkippingText.md',
                    // Week 4
                    'Online-Question/Week4/2Input.md',
                    'Online-Question/Week4/Airport.md',
                    'Online-Question/Week4/BasicCondition.md',
                    'Online-Question/Week4/BasicConditionV2.md',
                    'Online-Question/Week4/HotCold.md',
                    'Online-Question/Week4/UpperLower.md',
                    // Week 5
                    'Online-Question/Week5/Arrow.md',
                    'Online-Question/Week5/AutoCorrect.md',
                    'Online-Question/Week5/BusinessGrowthV1.md',
                    'Online-Question/Week5/BusinessGrowthV2.md',
                    'Online-Question/Week5/Congratulations.md',
                    'Online-Question/Week5/Count-AEIOU.md',
                    'Online-Question/Week5/DecimalConverter.md',
                    'Online-Question/Week5/EvenNumber.md',
                    'Online-Question/Week5/Hardcore-aN.md',
                    'Online-Question/Week5/IlluminatiConfirmed.md',
                    'Online-Question/Week5/LastTransaction.md',
                    'Online-Question/Week5/M2N.md',
                    'Online-Question/Week5/OddIsWinner.md',
                    'Online-Question/Week5/PascalTriangle.md',
                    'Online-Question/Week5/Pyramid.md',
                    'Online-Question/Week5/PyramidV2.md',
                    'Online-Question/Week5/ReversedPyramid.md',
                    'Online-Question/Week5/STIC2017.md',
                    'Online-Question/Week5/SumOfEvenOrOdd.md',
                    'Online-Question/Week5/SumOfN.md',
                    'Online-Question/Week5/Triangle.md',
                    'Online-Question/Week5/WeakTransmission.md',
                    // Week 6
                    'Online-Question/Week6/BasicList.md',
                    'Online-Question/Week6/BasicList2.md',
                    'Online-Question/Week6/BasicList3.md',
                    'Online-Question/Week6/BasicList4.md',
                    'Online-Question/Week6/BasicList5.md',
                    'Online-Question/Week6/CSVRead.md',
                    'Online-Question/Week6/DescendantsOfTheSun.md',
                    'Online-Question/Week6/GradeX.md',
                    'Online-Question/Week6/TimeMachine.md',
                ]
            },

            {
                title: 'Onsite Quiz',
                collapsable: true,
                children: [
                    // Week 1
                    'Onsite-Quiz/Week1/AreaWhereCircleAndSquareLiesOn.md',
                    'Onsite-Quiz/Week1/Cinema.md',
                    'Onsite-Quiz/Week1/Lost.md',
                    'Onsite-Quiz/Week1/NthDigit.md',
                    'Onsite-Quiz/Week1/Radar.md',
                    'Onsite-Quiz/Week1/SleepTime.md',
                    'Onsite-Quiz/Week1/WeaponFire.md',
                    // Week 2
                    'Onsite-Quiz/Week2/AtBashCipher.md',
                    'Onsite-Quiz/Week2/ClimbingStair.md',
                    'Onsite-Quiz/Week2/CountType.md',
                    'Onsite-Quiz/Week2/Diamonds.md',
                    'Onsite-Quiz/Week2/Duplicates.md',
                    'Onsite-Quiz/Week2/MyMoney.md',
                    'Onsite-Quiz/Week2/Plagarism.md',
                    'Onsite-Quiz/Week2/SecurityLevel.md',
                    // Week 3
                    'Onsite-Quiz/Week3/IntegerOnly.md',
                    'Onsite-Quiz/Week3/PunchTheOddDriveTheEven.md',
                    'Onsite-Quiz/Week3/SevenEleven.md',
                    'Onsite-Quiz/Week3/SortAgain.md',
                    'Onsite-Quiz/Week3/TagName.md',
                ]
            },

        ],

        // Search bar
        searchMaxSuggestions: 20
    }
}
