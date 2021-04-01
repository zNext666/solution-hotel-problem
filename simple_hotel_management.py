# using python 3 to run this script
import time

# Booking class
# id,room_id,checkin,checkout


class Booking:
    bookingList = []

    def __init__(self, room_id, checkin, checkout) -> None:
        self.id = len(Booking.bookingList)+1
        self.room_id = int(room_id)
        self.checkin = int(checkin)
        self.checkout = int(checkout)
        Booking.bookingList.append(self)
        # check if conflict will remove the booking
        Booking.isConflict(self)

    def __str__(self) -> str:
        return 'Booking Id %d: %d -> %d' % (self.id, self.checkin, self.checkout)

    def isConflict(self) -> None:
        for booking in Booking.bookingList:
            # be careful with <= and <
            # 2~3 hr to resolve this problem :(
            if booking.room_id == self.room_id and booking.checkin < self.checkin < booking.checkout and booking.checkin < self.checkout < booking.checkout:
                Booking.cancel_booking(self.id-1)

    def cancel_booking(bookid) -> None:
        Booking.bookingList.pop(int(bookid))


# Room class
# id,name
class Room:
    roomsList = []

    def __init__(self, room_name) -> None:
        self.id = len(Room.roomsList)+1
        self.room_name = room_name
        Room.roomsList.append(self)

    def __str__(self) -> str:
        return 'Room: %s' % (self.room_name)


# main
if __name__ == '__main__':
    # Measure elapsed time
    start = time.time()

    # n = int(input())

    # read example case
    case = open('./case02.txt', 'r')
    line = case.readlines()

    n = int(line[0])
    line.pop(0)

    # loop into N times
    for i in range(n):
        # command = input()

        # read command from file
        command = line[i]
        command = command.split()
        # python didn't have switch case, So sad :(
        if command[0] == 'create' and command[1] == 'room':
            Room(command[2])
        elif command[0] == 'book':
            Booking(command[1], command[2], command[3])
        elif command[0] == 'cancel':
            Booking.cancel_booking(int(command[1])-1)
        else:
            # Handle unknows command
            print('unknows command')

    # print the result HERE !
    for i in Room.roomsList:
        print(i)
        for j in Booking.bookingList:
            if(i.id == j.room_id):
                print(j)

    end = time.time()
    print('Elapsed time: %f' % (end - start))
