import copy
import os

import matplotlib.pyplot as plt
import matplotlib.patches as patches
simulation_period = 200


def first_come_first_served(processes):
    gantt_chart = []
    ready_queue = []
    waiting_queue = []
    finished_flag = True

    for i in range(simulation_period):  # time

        processes_arrived = [process for process in processes if process.arrival_time <= i]
        # Iterate over the processes that meet the condition
        for process in processes_arrived:
            process.wait_time[0] = i  # Update the wait time of the process to the current time 'i'
            ready_queue.append(processes.pop(processes.index(process)))

            # Create a list of processes that finish waiting time
        processes_finish_waiting = [process for process in waiting_queue if
                                    process.come_back_after + process.completion_time[0] <= i]
        # Iterate over the processes that meet the condition
        for process in processes_finish_waiting:
            process.wait_time[0] = i  # Update the wait time of the process to the current time 'i'
            ready_queue.append(
                waiting_queue.pop(waiting_queue.index(process)))  # Move the process from waiting_queue to ready_queue

        if finished_flag:  #if the previous process finished get another
            if len(ready_queue) == 0:  #if there is no processes then empty time
                gantt_chart.append(" ")
                continue
            executing_process = ready_queue.pop(0)  #pop the first element that arrived

            executing_process.wait_time[1] = i  # store the end time
            executing_process.wait_time[2] += (executing_process.wait_time[1] - executing_process.wait_time[0])

            finished_flag = False

        if executing_process.remaining_time > 0:
            executing_process.remaining_time -= 1
            gantt_chart.append(executing_process.name)

        if executing_process.remaining_time == 0:
            finished_flag = True
            executing_process.completion_time[0] = i+1
            executing_process.remaining_time = executing_process.burst_time
            waiting_queue.append(copy.copy(executing_process))

    executing_process.completion_time[0] = simulation_period
    return gantt_chart


def shortest_job_first(processes):

    gantt_chart = []
    ready_queue = []
    waiting_queue = []
    finished_flag = True

    for i in range(simulation_period):  # time

        processes_arrived = [process for process in processes if process.arrival_time <= i]
        # Iterate over the processes that meet the condition
        for process in processes_arrived:
            process.wait_time[0] = i  # Update the wait time of the process to the current time 'i'
            ready_queue.append(processes.pop(processes.index(process)))

            # Create a list of processes that finish waiting time
        processes_finish_waiting = [process for process in waiting_queue if
                                    process.come_back_after + process.completion_time[0] <= i]
        # Iterate over the processes that meet the condition
        for process in processes_finish_waiting:
            process.wait_time[0] = i  # Update the wait time of the process to the current time 'i'
            ready_queue.append(
                waiting_queue.pop(waiting_queue.index(process)))  # Move the process from waiting_queue to ready_queue

        if finished_flag:  #if the previous process finished get another
            shortest_process_index = 0  #serching for the index that's process has the shortest time
            for j in range(len(ready_queue)):
                if ready_queue[shortest_process_index].burst_time > ready_queue[j].burst_time:
                    shortest_process_index = j

            if len(ready_queue) == 0:  #if there is no processes then empty time
                gantt_chart.append(" ")
                continue
            executing_process = ready_queue.pop(shortest_process_index)  #get the process that has the minimum burst time
            executing_process.wait_time[1] = i  # store the end time
            executing_process.wait_time[2] += (executing_process.wait_time[1] - executing_process.wait_time[0])
            finished_flag = False

        if executing_process.remaining_time > 0:
            executing_process.remaining_time -= 1
            gantt_chart.append(executing_process.name)

        if executing_process.remaining_time == 0:
            finished_flag = True
            executing_process.completion_time[0] = i+1
            executing_process.remaining_time = executing_process.burst_time
            waiting_queue.append(copy.copy(executing_process))

    executing_process.completion_time[0] = simulation_period
    return gantt_chart


def shortest_remaining_first(processes):

    gantt_chart = []
    ready_queue = []
    waiting_queue = []
    finished = True

    for i in range(simulation_period):  # time

        processes_arrived = [process for process in processes if process.arrival_time <= i]
        # Iterate over the processes that meet the condition
        for process in processes_arrived:
            process.wait_time[0] = i  # Update the wait time of the process to the current time 'i'
            ready_queue.append(processes.pop(processes.index(process)))

            # Create a list of processes that finish waiting time
        processes_finish_waiting = [process for process in waiting_queue if
                                    process.come_back_after + process.completion_time[0] <= i]
        # Iterate over the processes that meet the condition
        for process in processes_finish_waiting:
            process.wait_time[0] = i  # Update the wait time of the process to the current time 'i'
            ready_queue.append(
                waiting_queue.pop(waiting_queue.index(process)))  # Move the process from waiting_queue to ready_queue

        if finished:  #if the previous process finished get the process that has the shortest remaining time

            if len(ready_queue) == 0:
                gantt_chart.append(" ")  #if there is no processes then empty time
                continue

            shortest_process_index = 0
            for j in range(len(ready_queue)):
                if ready_queue[shortest_process_index].remaining_time > ready_queue[j].remaining_time:
                    shortest_process_index = j

            executing_process = ready_queue.pop(shortest_process_index)
            executing_process.wait_time[1] = i  # store the end time
            executing_process.wait_time[2] += (executing_process.wait_time[1] - executing_process.wait_time[0])

        else:  #compare the current executing process with the processes in the ready
            swap = False
            for j in range(len(ready_queue)):

                if executing_process.remaining_time > ready_queue[j].remaining_time:
                    shortest_process_index = j
                    swap = True

            if swap:  #if there is a process that has shorter remaining time then switch them
                executing_process.wait_time[0] = i  # store the start time
                ready_queue.append(copy.copy(executing_process))

                executing_process = ready_queue.pop(shortest_process_index)
                executing_process.wait_time[1] = i  # store the end time
                executing_process.wait_time[2] += (executing_process.wait_time[1] - executing_process.wait_time[0])

        if executing_process.remaining_time > 0:
            executing_process.remaining_time -= 1
            executing_process.completion_time[0] = (i + 1)  # it may be the last time to be in the cpu
            gantt_chart.append(executing_process.name)
            finished = False

        if executing_process.remaining_time == 0:
            finished = True
            executing_process.completion_time[0] = i+1

            executing_process.remaining_time = executing_process.burst_time
            waiting_queue.append(copy.copy(executing_process))

    executing_process.completion_time[0] = simulation_period
    return gantt_chart


def round_robin(processes, quantum=5):

    gantt_chart = []
    ready_queue = []
    waiting_queue = []
    switch = True
    q = 0

    for i in range(simulation_period):  # time

        processes_arrived = [process for process in processes if process.arrival_time <= i]
        # Iterate over the processes that meet the condition
        for process in processes_arrived:
            process.wait_time[0] = i  # Update the wait time of the process to the current time 'i'
            ready_queue.append(processes.pop(processes.index(process)))

            # Create a list of processes that finish waiting time
        processes_finish_waiting = [process for process in waiting_queue if
                                    process.come_back_after + process.completion_time[0] <= i]
        # Iterate over the processes that meet the condition
        for process in processes_finish_waiting:
            process.wait_time[0] = i  # Update the wait time of the process to the current time 'i'
            ready_queue.append(
                waiting_queue.pop(waiting_queue.index(process)))  # Move the process from waiting_queue to ready_queue

        if switch:  #if we need to get a process
            if len(ready_queue) == 0:
                gantt_chart.append(" ")
                continue
            executing_process = ready_queue.pop(0)
            executing_process.wait_time[1] = i  # store the end time
            executing_process.wait_time[2] += (executing_process.wait_time[1] - executing_process.wait_time[0])

        if executing_process.remaining_time > 0:
            executing_process.remaining_time -= 1
            executing_process.completion_time[0] = (i + 1)  # it may be the last time to be in the cpu
            q += 1
            gantt_chart.append(executing_process.name)

            if q == quantum:  #if it finishes the round time
                switch = True
                q = 0
                if executing_process.remaining_time != 0:  #if the current process not finish its burst time append it to the ready
                    executing_process.wait_time[0] = i + 1  # store the start time it start in the ready queue from the next time unit
                    ready_queue.append(copy.copy(executing_process))

            else:  #round time does not finish
                switch = False

        if executing_process.remaining_time == 0:
            switch = True
            q = 0  #reset the round timer
            executing_process.completion_time[0] = i+1

            executing_process.remaining_time = executing_process.burst_time
            waiting_queue.append(copy.copy(executing_process))

    executing_process.completion_time[0] = simulation_period

    return gantt_chart


def preemptive_priority(processes, aging=999999):
    gantt_chart = []
    ready_queue = []
    waiting_queue = []
    finished = True

    for i in range(simulation_period):  # time

        for process in ready_queue:  # check the processes to increase their priority
            process.ready_time += 1
            if process.ready_time % aging == 0 and process.current_priority != 0:
                process.current_priority -= 1

        processes_arrived = [process for process in processes if process.arrival_time <= i]
        # Iterate over the processes that meet the condition
        for process in processes_arrived:
            process.wait_time[0] = i  # Update the wait time of the process to the current time 'i'
            ready_queue.append(processes.pop(processes.index(process)))

            # Create a list of processes that finish waiting time
        processes_finish_waiting = [process for process in waiting_queue if
                                    process.come_back_after + process.completion_time[0] <= i]
        # Iterate over the processes that meet the condition
        for process in processes_finish_waiting:
            process.wait_time[0] = i  # Update the wait time of the process to the current time 'i'
            ready_queue.append(
                waiting_queue.pop(waiting_queue.index(process)))  # Move the process from waiting_queue to ready_queue

        if finished:  #if the previous process finished get the process that has the highest priority

            if len(ready_queue) == 0:  #if there is no processes then empty time
                gantt_chart.append(" ")
                continue

            highest_priority_index = 0  #serching for the process that has the highest priority
            for j in range(len(ready_queue)):
                if ready_queue[highest_priority_index].current_priority > ready_queue[j].current_priority:
                    highest_priority_index = j

            executing_process = ready_queue.pop(highest_priority_index)
            executing_process.wait_time[1] = i  # store the end time
            executing_process.wait_time[2] += (executing_process.wait_time[1] - executing_process.wait_time[0])

        else:  #compare the current executing process with the processes in the ready
            swap = False
            for j in range(len(ready_queue)):
                if executing_process.current_priority > ready_queue[j].current_priority:
                    highest_priority_index = j
                    swap = True

            if swap:  #if there is a process that has higher priority then switch them
                executing_process.wait_time[0] = i  # store the start time
                ready_queue.append(copy.copy(executing_process))
                executing_process = ready_queue.pop(highest_priority_index)
                executing_process.wait_time[1] = i  # store the end time
                executing_process.wait_time[2] += (executing_process.wait_time[1] - executing_process.wait_time[0])

        if executing_process.remaining_time > 0:
            executing_process.remaining_time -= 1
            executing_process.completion_time[0] = (i + 1)  # it may be the last time to be in the cpu
            gantt_chart.append(executing_process.name)
            finished = False

        if executing_process.remaining_time == 0:
            finished = True
            executing_process.completion_time[0] = i + 1

            executing_process.remaining_time = executing_process.burst_time
            executing_process.current_priority = executing_process.priority  #reset its priority
            waiting_queue.append(copy.copy(executing_process))

    executing_process.completion_time[0] = simulation_period
    return gantt_chart


def non_preemptive_priority(processes, aging=99999999):

    gantt_chart = []
    ready_queue = []
    waiting_queue = []
    finished_flag = True

    for i in range(simulation_period):  # time

        for process in ready_queue:  #check the processes to increase their priority
            process.ready_time += 1
            if process.ready_time % aging == 0 and process.current_priority != 0:
                process.current_priority -= 1

        processes_arrived = [process for process in processes if process.arrival_time <= i]
        # Iterate over the processes that meet the condition
        for process in processes_arrived:
            process.wait_time[0] = i  # Update the wait time of the process to the current time 'i'
            ready_queue.append(processes.pop(processes.index(process)))

            # Create a list of processes that finish waiting time
        processes_finish_waiting = [process for process in waiting_queue if
                                    process.come_back_after + process.completion_time[0] <= i]
        # Iterate over the processes that meet the condition
        for process in processes_finish_waiting:
            process.wait_time[0] = i  # Update the wait time of the process to the current time 'i'
            ready_queue.append(
                waiting_queue.pop(waiting_queue.index(process)))  # Move the process from waiting_queue to ready_queue

        if finished_flag:  #if the previous process finished get the process that has the highest priority

            highest_process_index = 0  #serching for the process that has the highest priority
            for j in range(len(ready_queue)):
                if ready_queue[highest_process_index].current_priority > ready_queue[j].current_priority:
                    highest_process_index = j

            if len(ready_queue) == 0:  #if there is no processes then empty time
                gantt_chart.append(" ")
                continue
            executing_process = ready_queue.pop(highest_process_index)
            executing_process.wait_time[1] = i  # store the end time
            executing_process.wait_time[2] += (executing_process.wait_time[1] - executing_process.wait_time[0])

            finished_flag = False

        if executing_process.remaining_time > 0:
            executing_process.remaining_time -= 1
            gantt_chart.append(executing_process.name)

        if executing_process.remaining_time == 0:
            finished_flag = True
            executing_process.completion_time[0] = i + 1
            executing_process.remaining_time = executing_process.burst_time
            executing_process.current_priority = executing_process.priority  #reset its priority
            waiting_queue.append(copy.copy(executing_process))

    executing_process.completion_time[0] = simulation_period
    return gantt_chart


def calculate_averages(processes):

    total_tat = 0
    total_wt = 0
    num_of_finished_processes = 0

    for process in processes:
        if process.completion_time[0] > 0:

            num_of_finished_processes += 1

            tat = process.completion_time[0] - process.arrival_time

            wt = process.wait_time[2]

            total_tat += tat
            total_wt += wt

            print(f"-){process.name} Turnaround Time = {tat}, Waiting Time = {wt} ")

        else:
            print(f"*){process.name} has not finished ")

    print(f"\n==> Average Turnaround Time = {total_tat/num_of_finished_processes:.3f}, Average Waiting Time = {total_wt/num_of_finished_processes:.3f}")


def draw(gantt_chart, approach):
    fig, ax = plt.subplots(figsize=(13, 5))

    color_mapping = {
        'P1': 'red',
        'P2': 'blue',
        'P3': 'green',
        'P4': 'yellow',
        'P5': 'orange',
        'P6': 'purple',
        'P7': 'brown',
        ' ': 'white',
    }
    current_string = gantt_chart[0]
    current_count = 1
    previous_count = 0

    for process in gantt_chart[1:]:
        # If the current string is the same as the previous one, increment the count
        if process == current_string:
            current_count += 1
        else:
            # Calculate the center of the rectangle based on the previous count and current count
            center_x = previous_count + current_count / 2

            # Draw a rectangle for the previous string with width equal to its count
            rectangle = patches.Rectangle((previous_count, 0), current_count, 0.5, edgecolor='black',
                                          facecolor=color_mapping[current_string])
            ax.add_patch(rectangle)
            # Add text to the rectangle
            text = current_string
            plt.text(center_x, 0.25, text, ha='center', va='center', fontsize=12, color='black')

            # Update variables for the new string
            current_string = process
            previous_count += current_count
            current_count = 1

    # Draw the last rectangle
    center_x = previous_count + current_count / 2
    rectangle = patches.Rectangle((previous_count, 0), current_count, 0.5, edgecolor='black',
                                  facecolor=color_mapping[current_string])
    ax.add_patch(rectangle)

    # Add text to the rectangle
    text = current_string
    plt.text(center_x, 0.25, text, ha='center', va='center', fontsize=12, color='black')

    # Set x-axis ticks at each unit
    x_ticks = [rect.get_x() for rect in ax.patches] + [rect.get_x() + rect.get_width() for rect in ax.patches]
    plt.xticks(sorted(x_ticks), rotation=45)

    ax.set_yticks([])
    ax.yaxis.set_visible(False)

    ax.set_xlim(0, previous_count + current_count)
    ax.set_ylim(0, 0.5)
    ax.set_xlabel('time')
    ax.set_title('Gantt chart for ' + approach)

    # Save the plot with the approach name as the filename
    if not os.path.exists("Gantt_Charts"):
        os.makedirs("Gantt_Charts")
    filename = f"{approach.replace(' ', '_')}.png"
    filepath = os.path.join("Gantt_Charts", filename)

    with open(filepath, 'w'):
        pass  #as a placeholder
    # Save the new plot
    plt.savefig(filepath)

    # Display the plot without blocking the execution
    plt.draw()
    plt.pause(0.001)
