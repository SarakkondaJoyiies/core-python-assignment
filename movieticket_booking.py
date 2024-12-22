
def managing_seats(total_seats, booked_seats, book_seat, cancel_seat):
    if book_seat not in booked_seats and 1 <= book_seat <= total_seats:
        booked_seats.append(book_seat)
        print(f"Seat {book_seat} booked.")
    else:
        print(f"Seat {book_seat} cannot be booked.")

    if cancel_seat in booked_seats:
        booked_seats.remove(cancel_seat)
        print(f"Seat {cancel_seat} cancelled.")
    else:
        print(f"Seat {cancel_seat} is not booked.")

    print("Available seats:", [seat for seat in range(1, total_seats + 1) if seat not in booked_seats])

total_seats = 10
booked_seats = [2, 5, 7]
managing_seats(total_seats, booked_seats, 3, 5)
