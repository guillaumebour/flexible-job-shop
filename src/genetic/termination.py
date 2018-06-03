#!/usr/bin/env python

# This module decides when the genetic algorithm should stop. We only use a
# maximum number of generations for now.

from src import config


def shouldTerminate(population, gen):
    return gen > config.maxGen
