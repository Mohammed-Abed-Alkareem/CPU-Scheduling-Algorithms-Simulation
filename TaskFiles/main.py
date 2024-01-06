import copy
from matplotlib import pyplot as plt
from Process import Process
import scheduling_algorithms as sa

# Creating instances for each process
processes = [
             Process(name="P1", arrival_time=0, burst_time=10, come_back_after=2, priority=3),
             Process(name="P2", arrival_time=1, burst_time=8, come_back_after=4, priority=2),
             Process(name="P3", arrival_time=3, burst_time=14, come_back_after=6, priority=3),
             Process(name="P4", arrival_time=4, burst_time=7, come_back_after=8, priority=1),
             Process(name="P5", arrival_time=6, burst_time=5, come_back_after=3, priority=0),
             Process(name="P6", arrival_time=7, burst_time=4, come_back_after=6, priority=1),
             Process(name="P7", arrival_time=8, burst_time=6, come_back_after=9, priority=2)
            ]


# First Come, First Served
print("\n\nFirst Come First Served:\n")
gantt_chart = sa.first_come_first_served(copy.copy(processes))
sa.calculate_averages(processes)
for process in processes:
    process.reset_attribute()

sa.draw(gantt_chart, "First Come First Served")

# Shortest Job First
print("\n\nShortest Job First:\n")
gantt_chart = sa.shortest_job_first(copy.copy(processes))
sa.calculate_averages(processes)
for process in processes:
    process.reset_attribute()

sa.draw(gantt_chart, "Shortest Job First")


# Shortest Remaining Time First
print("\n\nShortest Remaining Time First:\n")
gantt_chart = sa.shortest_remaining_first(copy.copy(processes))
sa.calculate_averages(processes)

for process in processes:
    process.reset_attribute()

sa.draw(gantt_chart, "Shortest Remaining Time First")


# Round Robin
print("\n\nRound Robin:\n")
gantt_chart = sa.round_robin(copy.copy(processes), quantum=5)
sa.calculate_averages(processes)
for process in processes:
    process.reset_attribute()

sa.draw(gantt_chart, "Round Robin")


#Preemptive Priority Scheduling with aging
print("\n\nPreemptive Priority Scheduling with aging:\n")
gantt_chart = sa.preemptive_priority(copy.copy(processes), aging=5)
sa.calculate_averages(processes)
for process in processes:
    process.reset_attribute()

sa.draw(gantt_chart, "Preemptive Priority Scheduling with aging")


# Non-preemptive Priority Scheduling with aging
print("\n\nNon-preemptive Priority Scheduling with aging:\n")
gantt_chart = sa.non_preemptive_priority(copy.copy(processes), aging=5)
sa.calculate_averages(processes)
for process in processes:
    process.reset_attribute()

sa.draw(gantt_chart, "Non-preemptive Priority Scheduling with aging")

# Keep the plots open until manually closed
plt.show()
