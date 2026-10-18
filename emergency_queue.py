
# Emergency Room Priority Queue
# Patients with lower urgency numbers are treated first.


class Patient:
    def __init__(self, name, urgency):
        if not isinstance(urgency, int) or not 1 <= urgency <= 10:
            raise ValueError("Urgency must be between 1 and 10.")

        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []

    # Move a new patient up if they have higher priority
    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.data[parent].urgency <= self.data[index].urgency:
                break

            self.data[parent], self.data[index] = (
                self.data[index], self.data[parent]
            )

            index = parent

    # Restore the heap after removing a patient
    def heapify_down(self, index):
        size = len(self.data)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left

            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (
                self.data[smallest], self.data[index]
            )

            index = smallest

    # Add a new patient
    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    # Display the current patient queue
    def print_heap(self):
        print("Current Queue:")

        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    # View the most urgent patient
    def peek(self):
        if not self.data:
            return None

        return self.data[0]

    # Remove the most urgent patient
    def remove_min(self):
        if not self.data:
            return None

        first = self.data[0]
        last = self.data.pop()

        if self.data:
            self.data[0] = last
            self.heapify_down(0)

        return first


# Test the emergency priority queue
if __name__ == "__main__":
    heap = MinHeap()

    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))

    heap.print_heap()

    print("\nNext patient:", heap.peek().name)

    served = heap.remove_min()
    print("Patient treated:", served.name)

    print("\nUpdated Queue:")
    heap.print_heap()

    assert heap.peek().name == "Jordan"
    print("\nEmergency queue testing complete.")
