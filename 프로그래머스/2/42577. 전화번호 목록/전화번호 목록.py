def solution(phone_book):
    phone_book.sort()
    for idx,pb in enumerate(phone_book):
        if pb == phone_book[-1]:
            return True
        if phone_book[idx+1][:len(pb)] == pb: 
            return False

    return True