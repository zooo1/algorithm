def solution(phone_book):
    phone_book_dict = dict()

    for number in phone_book:

        if number in phone_book_dict:
            return False
        else:
            for key in phone_book_dict.keys():
                if key == number[:len(key)] or number == key[:len(number)]:
                    return False
            phone_book_dict[number] = 1
    return True