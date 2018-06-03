#!/usr/bin/env python

import sys


def split_ms(pb_instance, ms):
    jobs = []
    current = 0
    for index, job in enumerate(pb_instance['jobs']):
        jobs.append(ms[current:current+len(job)])
        current += len(job)
    return jobs


def get_processing_time(op_by_machine, machine_nb):
    for op in op_by_machine:
        if op['machine'] == machine_nb:
            return op['processingTime']
    print("[ERROR] Machine {} doesn't to be able to process this task.".format(machine_nb))
    sys.exit(-1)


def is_free(tab, start, duration):
    for k in range(start, start+duration):
        if not tab[k]:
            return False
    return True


def find_first_available_place(start_ctr, duration, machine_jobs):
    max_duration_list = []
    max_duration = start_ctr + duration

    # max_duration is either the start_ctr + duration or the max(possible starts) + duration
    if machine_jobs:
        for job in machine_jobs:
            max_duration_list.append(job[3] + job[1])  # start + process time

        max_duration = max(max(max_duration_list), start_ctr) + duration

    machine_used = [True] * max_duration

    # Updating array with used places
    for job in machine_jobs:
        start = job[3]
        long = job[1]
        for k in range(start, start + long):
            machine_used[k] = False

    # Find the first available place that meets constraint
    for k in range(start_ctr, len(machine_used)):
        if is_free(machine_used, k, duration):
            return k


def decode(pb_instance, os, ms):
    o = pb_instance['jobs']
    machine_operations = [[] for i in range(pb_instance['machinesNb'])]

    ms_s = split_ms(pb_instance, ms)  # machine for each operations

    indexes = [0] * len(ms_s)
    start_task_cstr = [0] * len(ms_s)

    # Iterating over OS to get task execution order and then checking in
    # MS to get the machine
    for job in os:
        index_machine = ms_s[job][indexes[job]]
        machine = o[job][indexes[job]][index_machine]['machine']
        prcTime = o[job][indexes[job]][index_machine]['processingTime']
        start_cstr = start_task_cstr[job]

        # Getting the first available place for the operation
        start = find_first_available_place(start_cstr, prcTime, machine_operations[machine - 1])
        name_task = "{}-{}".format(job, indexes[job]+1)

        machine_operations[machine - 1].append((name_task, prcTime, start_cstr, start))

        # Updating indexes (one for the current task for each job, one for the start constraint
        # for each job)
        indexes[job] += 1
        start_task_cstr[job] = (start + prcTime)

    return machine_operations


def translate_decoded_to_gantt(machine_operations):
    data = {}

    for idx, machine in enumerate(machine_operations):
        machine_name = "Machine-{}".format(idx + 1)
        operations = []
        for operation in machine:
            operations.append([operation[3], operation[3] + operation[1], operation[0]])

        data[machine_name] = operations

    return data
