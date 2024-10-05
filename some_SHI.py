def main(table):
    return [
        [
            ' '.join(
                reversed(person[0].split())
            ), person[1][4:], '0' if person[2] == 'N' else '1'
        ] for person in [
            [name, *phone.split(':')] for name, phone in [
                list(
                    dict.fromkeys(row)
                ) for row in list(
                    filter(
                        len, map(lambda row: list(filter(bool, row)), table)
                    )
                )
            ]
        ]
    ]


table = [
    ['Иван Гутяк', None, '777-694-6944:N', 'Иван Гутяк'],
    ['Вячеслав Цочивли', None, '517-058-2076:Y', 'Вячеслав Цочивли'],
    [None, None, None, None],
    [None, None, None, None],
    ['Максим Чушко', None, '847-349-4551:N', 'Максим Чушко'],
]

print("\nC'mon my nigga:")
print(main(table))
