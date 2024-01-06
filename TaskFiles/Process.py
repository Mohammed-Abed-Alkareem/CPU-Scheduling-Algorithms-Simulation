class Process:
    def __init__(self, name, arrival_time, burst_time, come_back_after=9999999, priority=0):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.come_back_after = come_back_after
        self.priority = priority
        self.current_priority = priority
        self.remaining_time = burst_time
        self.wait_time = [0, 0, 0]  # start , end , total
        self.completion_time = [0]
        self.ready_time = 0

    def print_info(self):
        print(f"{self.name}: Turnaround Time: {self.turnaround_time} ")

    def print_name(self):
        print(f"{self.name}")

    def reset_attribute(self):
        self.remaining_time = self.burst_time
        self.wait_time = [0, 0, 0]
        self.ready_time = 0
        self.completion_time = [0]
        self.current_priority = self.priority
