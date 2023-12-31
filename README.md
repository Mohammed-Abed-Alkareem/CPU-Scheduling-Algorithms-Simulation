# CPU-Scheduling-Algorithms-Simulation
Simulation for CPU Scheduling Algorithms with plotting Gantt-Chart

# Summary

Creating a scheduling algorithm simulation project involves implementing various scheduling algorithms, generating Gantt charts, and calculating average waiting time and average turnaround time.

# Specifications
## Scheduling Algorithms:

- First-Come, First-Serve (FCFS)
- Shortest Job First (SJF)
- Priority Scheduling
- Round Robin (RR)
- Preemptive Priority Scheduling, with aging
- Non-preemptive Priority Scheduling, with aging

## Process Details:

- Arrival Time: The time at which a process arrives in the ready queue.
- Burst Time: The time required by a process for execution.
- Comes back after: The interval or time duration after which a process returns to the ready queue after completing execution.
- Priority: The priority assigned to a process, relevant for Priority Scheduling.
### Once each process is done processing its “Burst Time”, it goes to the waiting queue, then “Comes back” to the ready queue after the "Comes back after".

## Input Representation
### Scenario 1 : with simuation period = 200 unit
| Process | Arrival Time | Burst Time | Comes back after | Priority |
|---------|--------------|------------|-------------------|----------|
| P1      | 0            | 10         | 2                 | 3        |
| P2      | 1            | 8          | 4                 | 2        |
| P3      | 3            | 14         | 6                 | 3        |
| P4      | 4            | 7          | 8                 | 1        |
| P5      | 6            | 5          | 3                 | 0        |
| P6      | 7            | 4          | 6                 | 1        |
| P7      | 8            | 6          | 9                 | 2        |


### Scenario 2: simulation untill all processes finish once
| Process | Arrival Time | Burst Time |  Priority |
|---------|--------------|------------|----------|
| P1      | 0            | 10         | 3        |
| P2      | 1            | 8          |  2        |
| P3      | 3            | 14         |  3        |
| P4      | 4            | 7          |  1        |
| P5      | 6            | 5          |  0        |
| P6      | 7            | 4          | 1        |
| P7      | 8            | 6          |  2        |



### Output

#### Gantt Charts

##### First-Come, First-Serve (FCFS)

![FCFS Gantt Chart](/Gantt_Charts/First_Come_First_Served_1.png)

##### Shortest Job First (SJF)

![SJN Gantt Chart](/Gantt_Charts/Shortest_Job_First_1.png)

##### Shortest Remaining Time First (SRTF)

![SJN Gantt Chart](/Gantt_Charts/Shortest_Remaining_Time_First_1.png)


##### Round Robin (RR)

![Round Robin Gantt Chart](/Gantt_Charts/Round_Robin_1.png)

##### Preemptive Priority Scheduling with aging = 5

![Preemptive Priority Scheduling Gantt Chart](/Gantt_Charts/Preemptive_Priority_Scheduling_with_aging_1.png)

##### Non-preemptive Priority Scheduling with aging = 5

![Non-preemptive Priority Scheduling Gantt Chart](/Gantt_Charts/Non-preemptive_Priority_Scheduling_with_aging_1.png)

#### Performance Metrics

##### First-Come, First-Serve (FCFS)

- P1 Turnaround Time = 172, Waiting Time = 126 
- P2 Turnaround Time = 179, Waiting Time = 135 
- P3 Turnaround Time = 191, Waiting Time = 117 
- P4 Turnaround Time = 196, Waiting Time = 145 
- P5 Turnaround Time = 146, Waiting Time = 125 
- P6 Turnaround Time = 149, Waiting Time = 125 
- P7 Turnaround Time = 154, Waiting Time = 118 

==> Average Turnaround Time = 169.571, Average Waiting Time = 127.286

##### Shortest Job First (SJF)

- P1 Turnaround Time = 10, Waiting Time = 0 
- P2 has not finished 
- P3 has not finished 
- P4 has not finished 
- P5 Turnaround Time = 193, Waiting Time = 92 
- P6 Turnaround Time = 187, Waiting Time = 63 
- P7 Turnaround Time = 192, Waiting Time = 11 

==> Average Turnaround Time = 145.5, Average Waiting Time = 41.5

  ##### Shortest Remaining Time First (SRTF)

- P1 Turnaround Time = 1, Waiting Time = 0 
- P2 Turnaround Time = 8, Waiting Time = 0 
- P3 has not finished 
- P4 has not finished 
- P5 Turnaround Time = 194, Waiting Time = 70 
- P6 Turnaround Time = 184, Waiting Time = 30 
- P7 Turnaround Time = 188, Waiting Time = 77 

==> Average Turnaround Time = 115 , Average Waiting Time = 35.4

##### Round Robin (RR)

- P1 Turnaround Time = 191, Waiting Time = 145 
- P2 Turnaround Time = 179, Waiting Time = 138 
- P3 Turnaround Time = 183, Waiting Time = 138 
- P4 Turnaround Time = 196, Waiting Time = 146 
- P5 Turnaround Time = 169, Waiting Time = 124 
- P6 Turnaround Time = 188, Waiting Time = 134 
- P7 Turnaround Time = 173, Waiting Time = 137 

==> Average Turnaround Time = 182.714, Average Waiting Time = 137.429

##### Preemptive Priority Scheduling with aging = 5

- P1 Turnaround Time = 184, Waiting Time = 138 
- P2 Turnaround Time = 199, Waiting Time = 161 
- P3 Turnaround Time = 195, Waiting Time = 121 
- P4 Turnaround Time = 170, Waiting Time = 118 
- P5 Turnaround Time = 155, Waiting Time = 126 
- P6 Turnaround Time = 149, Waiting Time = 125 
- P7 Turnaround Time = 159, Waiting Time = 123 

==> Average Turnaround Time = 173, Average Waiting Time = 130.286

##### Non-preemptive Priority Scheduling with aging = 5

- P1 Turnaround Time = 172, Waiting Time = 126
- P2 Turnaround Time = 186, Waiting Time = 142
- P3 Turnaround Time = 197, Waiting Time = 124
- P4 Turnaround Time = 175, Waiting Time = 123
- P5 Turnaround Time = 146, Waiting Time = 125
- P6 Turnaround Time = 149, Waiting Time = 125
- P7 Turnaround Time = 154, Waiting Time = 118 

==> Average Turnaround Time = 168.429, Average Waiting Time = 126.143
  
# Authors

### Mohammed Abed Alkareem

