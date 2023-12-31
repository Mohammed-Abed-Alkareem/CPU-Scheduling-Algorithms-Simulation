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

- Average Waiting Time: X units
- Average Turnaround Time: Y units

##### Shortest Job Next (SJN)

- Average Waiting Time: X units
- Average Turnaround Time: Y units

##### Round Robin (RR)

- Average Waiting Time: X units
- Average Turnaround Time: Y units

##### Preemptive Priority Scheduling with aging = 5

- Average Waiting Time: X units
- Average Turnaround Time: Y units

##### Non-preemptive Priority Scheduling with aging = 5

- Average Waiting Time: X units
- Average Turnaround Time: Y units
  
# Authors

### Mohammed Abed Alkareem

