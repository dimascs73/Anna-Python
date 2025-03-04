def is_lucky_ticket(number):
    str_num = f'{number:06}'

    first_half_sum = sum(int(digit) for digit in str_num[:3])

    second_half_sum = sum(int(digit) for digit in str_num[(len(str_num) -1):(len(str_num)-4):-1])

    return first_half_sum == second_half_sum


def lucky(ticket):
    global lastTicket

    current_is_lucky = is_lucky_ticket(ticket)
    previous_is_lucky = is_lucky_ticket(lastTicket)

    if current_is_lucky and previous_is_lucky:
        return 'Счастливый'
    else:
        return 'Несчастливый'
    
lastTicket = 123213
print(lucky(102111))