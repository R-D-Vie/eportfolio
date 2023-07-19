def towers_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    towers_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    towers_of_hanoi(n - 1, auxiliary, destination, source)


# Testing the towers_of_hanoi function
num_disks = 8
towers_of_hanoi(num_disks, 'A', 'C', 'B')
