def written_number_to_digit(written_number):
    # Define a list of written numbers and their corresponding digits
    number_list = [
        ('one', '1'),
        ('two', '2'),
        ('three', '3'),
        ('four', '4'),
        ('five', '5'),
        ('six', '6'),
        ('seven', '7'),
        ('eight', '8'),
        ('nine', '9'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9')
    ]

    for word, digit in number_list:
        if word in written_number:
            return digit

    return -1
