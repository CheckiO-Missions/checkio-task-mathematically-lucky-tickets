"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "000000",
            "answer": True,
            "explanation": None
        },
        {
            "input": "707409",
            "answer": True,
            "explanation": None
        },
        {
            "input": "595347",
            "answer": False,
            "explanation": "(5 + ((9 * 5) + (3 + 47))) = 100"
        },
        {
            "input": "271353",
            "answer": False,
            "explanation": "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
        },
        {
            "input": "000955",
            "answer": False,
            "explanation": "(0 + (0 + (0 + (95 + 5)))) = 100"
        },
        {
            "input": "100478",
            "answer": True,
            "explanation": None
        },
        {
            "input": "100479",
            "answer": False,
            "explanation": "(1 + (0 + (0 + ((4 + 7) * 9)))) = 100"
        },
        {
            "input": "725126",
            "answer": True,
            "explanation": None
        },
        {
            "input": "836403",
            "answer": False,
            "explanation": "(8 * ((3 / 6) + (4 * 03))) = 100"
        },
        {
            "input": "240668",
            "answer": False,
            "explanation": "(2 + (40 + (66 - 8))) = 100"
        },
        {
            "input": "082140",
            "answer": True,
            "explanation": None
        },
        {
            "input": "574699",
            "answer": False,
            "explanation": "(5 - ((7 * (4 - 6)) - (9 * 9))) = 100"
        },
        {
            "input": "324347",
            "answer": False,
            "explanation": "(3 + ((2 * 43) + (4 + 7))) = 100"
        },
        {
            "input": "064377",
            "answer": True,
            "explanation": None
        },
        {
            "input": "111111",
            "answer": False,
            "explanation": "(1 * (111 - 11)) = 100"
        },
        {
            "input": "555555",
            "answer": False,
            "explanation": "(5 + ((5 * ((5 * 5) - 5)) - 5)) = 100"
        },
        {
            "input": "777777",
            "answer": False,
            "explanation": "((7 + 7) * (7 + (7 / (7 * 7)))) = 100"
        },
        {
            "input": "392039",
            "answer": False,
            "explanation": "((3 + 9) * ((2 / (0 - 3)) + 9)) = 100"
        }
    ],
    "Extra": [
        {
            "input": "712922",
            "answer": False,
            "explanation": "(7 + (1 + (2 + (92 - 2)))) = 100"
        },
        {
            "input": "142686",
            "answer": False,
            "explanation": "(1 * (4 + ((2 + (6 + 8)) * 6))) = 100"
        },
        {
            "input": "980072",
            "answer": False,
            "explanation": "(9 * (800 / 72)) = 100"
        },
        {
            "input": "141463",
            "answer": False,
            "explanation": "(1 + ((4 * (1 * (4 * 6))) + 3)) = 100"
        },
        {
            "input": "083881",
            "answer": False,
            "explanation": "(0 + (8 + (3 + (8 + 81)))) = 100"
        },
        {
            "input": "900948",
            "answer": True,
            "explanation": None
        },
        {
            "input": "963181",
            "answer": False,
            "explanation": "(9 + (6 + (3 + (1 + 81)))) = 100"
        },
        {
            "input": "133289",
            "answer": False,
            "explanation": "(1 + (3 * (32 - (8 - 9)))) = 100"
        },
        {
            "input": "193015",
            "answer": False,
            "explanation": "(1 + (93 + (0 + (1 + 5)))) = 100"
        },
        {
            "input": "677838",
            "answer": False,
            "explanation": "(6 + ((7 * (7 + 8)) - (3 + 8))) = 100"
        },
        {
            "input": "279216",
            "answer": False,
            "explanation": "(2 + (7 * (9 - (2 - (1 + 6))))) = 100"
        },
        {
            "input": "923897",
            "answer": False,
            "explanation": "(9 + (((2 * (3 + 8)) - 9) * 7)) = 100"
        },
        {
            "input": "313159",
            "answer": False,
            "explanation": "((3 * (1 + 31)) - (5 - 9)) = 100"
        },
        {
            "input": "353525",
            "answer": False,
            "explanation": "(3 * ((5 / (3 / 5)) + 25)) = 100"
        },
        {
            "input": "103818",
            "answer": False,
            "explanation": "(1 + (0 + ((3 + 8) * (1 + 8)))) = 100"
        },
        {
            "input": "686997",
            "answer": False,
            "explanation": "(6 + (8 - (6 - (99 - 7)))) = 100"
        },
        {
            "input": "884993",
            "answer": False,
            "explanation": "(8 + (8 + (4 * (9 + (9 + 3))))) = 100"
        },
        {
            "input": "064027",
            "answer": True,
            "explanation": None
        },
        {
            "input": "237867",
            "answer": False,
            "explanation": "(23 + (78 + (6 - 7))) = 100"
        },
        {
            "input": "874098",
            "answer": False,
            "explanation": "((8 * 7) + ((4 * 09) + 8)) = 100"
        },
        {
            "input": "173403",
            "answer": False,
            "explanation": "(1 + ((73 - 40) * 3)) = 100"
        },
        {
            "input": "907029",
            "answer": False,
            "explanation": "(90 - (70 / (2 - 9))) = 100"
        },
        {
            "input": "244247",
            "answer": False,
            "explanation": "(2 + (4 + (4 / (2 / 47)))) = 100"
        },
        {
            "input": "483989",
            "answer": False,
            "explanation": "(4 + (8 * (3 + ((9 - 8) * 9)))) = 100"
        },
        {
            "input": "743870",
            "answer": True,
            "explanation": None
        },
        {
            "input": "048581",
            "answer": False,
            "explanation": "(0 + (4 + (8 * (5 + (8 - 1))))) = 100"
        },
        {
            "input": "846763",
            "answer": False,
            "explanation": "(8 + ((4 + (6 * 7)) * (6 / 3))) = 100"
        },
        {
            "input": "941337",
            "answer": False,
            "explanation": "(9 + ((4 + (1 / 3)) * (3 * 7))) = 100"
        },
        {
            "input": "107006",
            "answer": True,
            "explanation": None
        },
        {
            "input": "174852",
            "answer": False,
            "explanation": "(1 * (74 + ((8 + 5) * 2))) = 100"
        },
        {
            "input": "095974",
            "answer": False,
            "explanation": "((0 * 9) + (5 * (9 + (7 + 4)))) = 100"
        },
        {
            "input": "811473",
            "answer": False,
            "explanation": "(8 * ((1 + (1 / 4)) * (7 + 3))) = 100"
        },
        {
            "input": "865210",
            "answer": False,
            "explanation": "((8 * 6) + (52 + (1 * 0))) = 100"
        },
        {
            "input": "001521",
            "answer": True,
            "explanation": None
        },
        {
            "input": "644506",
            "answer": False,
            "explanation": "((6 + 4) * (4 + ((5 * 0) + 6))) = 100"
        },
        {
            "input": "640340",
            "answer": True,
            "explanation": None
        },
        {
            "input": "090544",
            "answer": True,
            "explanation": None
        },
        {
            "input": "925375",
            "answer": False,
            "explanation": "(9 + ((2 * (5 + 3)) + 75)) = 100"
        },
        {
            "input": "594881",
            "answer": False,
            "explanation": "(5 + (94 + (8 - (8 - 1)))) = 100"
        },
        {
            "input": "300104",
            "answer": True,
            "explanation": None
        },
        {
            "input": "064605",
            "answer": True,
            "explanation": None
        }
    ]
}
