#!/usr/bin/env python

from src.genetic import genetic, encoding

# This script runs every non-trivial piece of code defined in this project to
# easily test their behavior

print("=== OS & MS generation ===")
op11 = [{'machine': 0, 'processingTime': 1}, {'machine': 1, 'processingTime': 2}]
op12 = [{'machine': 1, 'processingTime': 1}, {'machine': 2, 'processingTime': 2}]
job1 = [op11, op12]
op21 = [{'machine': 2, 'processingTime': 1}, {'machine': 3, 'processingTime': 2}]
op22 = [{'machine': 3, 'processingTime': 1}, {'machine': 4, 'processingTime': 2}]
job2 = [op21, op22]
op31 = [{'machine': 4, 'processingTime': 1}, {'machine': 5, 'processingTime': 2}]
op32 = [{'machine': 5, 'processingTime': 1}, {'machine': 0, 'processingTime': 2}]
job3 = [op31, op32]
jobs = [job1, job2, job3]
print("OS: " + str(encoding.generateOS({'machinesNb': 6, 'jobs': jobs})))
print("MS: " + str(encoding.generateMS({'machinesNb': 6, 'jobs': jobs})))

print("=== SELECTION ===")
pop = [([1, 3, 1, 2, 2, 3], [2, 1, 3, 1, 2, 2]),
       ([1, 1, 2, 2, 3, 3], [1, 2, 3, 1, 2, 3]),
       ([3, 2, 1, 1, 2, 3], [1, 1, 1, 1, 1, 1])]
print("elitist: " + str(genetic.elitistSelection(pop)))
print("tournament: " + str(genetic.tournamentSelection(pop)))

print("=== MUTATION ===")
p = [0, 1, 2, 3, 4, 5]

op11 = [{'machine': 0, 'processingTime': 1}, {'machine': 1, 'processingTime': 2}]
op12 = [{'machine': 1, 'processingTime': 1}, {'machine': 2, 'processingTime': 2}]
job1 = [op11, op12]
op21 = [{'machine': 2, 'processingTime': 1}, {'machine': 3, 'processingTime': 2}]
op22 = [{'machine': 3, 'processingTime': 1}, {'machine': 4, 'processingTime': 2}]
job2 = [op21, op22]
op31 = [{'machine': 4, 'processingTime': 1}, {'machine': 5, 'processingTime': 2}]
op32 = [{'machine': 5, 'processingTime': 1}, {'machine': 0, 'processingTime': 2}]
job3 = [op31, op32]
jobs = [job1, job2, job3]
print("swapping: " + str(genetic.swappingMutation(p)))
print("neighborghood: " + str(genetic.neighborhoodMutation(p)))
print("half: " + str(genetic.halfMutation(p, {'machinesNb': 6, 'jobs': jobs})))

print("=== CROSSOVER ===")
p1 = [1, 3, 1, 2, 2, 3]
p2 = [3, 2, 1, 2, 3, 1]
print("POX: " + str(genetic.precedenceOperationCrossover(p1, p2, {'jobs': range(10)})))
print("JBX: " + str(genetic.jobBasedCrossover(p1, p2, {'jobs': range(10)})))
print("two point: " + str(genetic.twoPointCrossover(p1, p2)))
