import time
import random
import statistics
#Константы (веса в граммах)
GOAL = 50000
NUM_RATS = 20
INITIAL_MIN_WT = 200
INITIAL_MAX_WT  = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS  = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500
# обеспечиваем для племенных пар четное число крыс
if NUM_RATS %2 != 0:
    NUM_RATS += 1

def populate(num_rats, min_wt, max_wt, mode_wt):
    """ Иницилиазация популяцию треугольным распределением весов"""
    return [int(random.triangular(min_wt, max_wt, mode_wt))for i in range(num_rats)]
def fitness(population, goal):
    """Измерить пригодность пополяции, основываясь на среднем значении атрибута относительно цели"""
    ave = statistics.mean(population)
    return ave / goal

def select(population, to_retain):
    """Отбраковать популяцию, оставив только заданное число ее членом"""
    sorted_population = sorted(population)
    to_retain_by_sex = to_retain//2
    members_per_sex = len(sorted_population) // 2
    females = sorted_population[:members_per_sex]
    males = sorted_population[members_per_sex:]
    selected_females = females[-to_retain_by_sex:]
    selected_males = males[-to_retain_by_sex:]
    return selected_males, selected_females
