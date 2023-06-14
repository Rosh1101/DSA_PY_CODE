def tower_hanoi(n,source,helper,destination):
    if n == 1:
        print("Shift 1st disk from ",source," to ", destination)
        return
    tower_hanoi(n-1,source,destination,helper)
    print("move the disk ", n, " from", source, " to", destination)
    tower_hanoi(n-1,helper,source,destination)
tower_hanoi(99,"s","h","d")