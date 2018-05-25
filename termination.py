# This module decides when the genetic algorithm should stop. We only use a
# maximum number of generations for now.

import config

def shouldTerminate(population, gen):
    return gen > config.maxGen
