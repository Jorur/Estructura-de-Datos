import heapq

estudiantes = []

heapq.heappush(estudiantes, (2, "A"))
heapq.heappush(estudiantes, (5, "B"))
heapq.heappush(estudiantes, (4, "C"))
heapq.heappush(estudiantes, (3, "D"))
heapq.heappush(estudiantes, (1, "E"))

while estudiantes:
    print(heapq.heappop(estudiantes))
