import time

A = [i for i in range(5, 0, -1)]
height = len(A) - 1  # Stable height value for animation
B = []
C = []

def move(n, source, target, auxiliary):
    if n > 0:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target
        target.append(source.pop())

        # Display our progress using a recursive function to draw it out
        draw_disks(A, B, C, height)
        print("")  # Provide spacing
        time.sleep(1)  # Pause for a moment to animate

        # Move the n - 1 disks that we left on auxiliary onto target
        move(n - 1, auxiliary, target, source)

def draw_disks(A, B, C, position, width=2 * int(max(A))):
    # width parameter defaults to double of the largest sized disk in the initial tower.
    if position >= 0:
        # If A has a value in the list at the given position, create a disk at its position (height)
        valueInA = " " if position >= len(A) else create_disk(A[position])
        # Same for B and C
        valueInB = " " if position >= len(B) else create_disk(B[position])
        valueInC = " " if position >= len(C) else create_disk(C[position])

        # Print each row
        print("{0:^{width}}{1:^{width}}{2:^{width}}".format(valueInA, valueInB, valueInC, width=width))

        # Recursively call this method again to the next position (height)
        draw_disks(A, B, C, position - 1, width)
    else:
        # When done with recursive, print column labels
        print("{0:^{width}}{1:^{width}}{2:^{width}}".format("A", "B", "C", width=width))

def create_disk(size):
    """Simple recursive method to create a slanted disk."""
    if size == 1:
        return "/\\"
    else:
        return "/" + create_disk(size - 1) + "\\"

# Initiate call from source A to target C with auxiliary B
move(len(A), A, C, B)