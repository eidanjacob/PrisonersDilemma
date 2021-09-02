from agent import *
import os
import csv
from datetime import datetime as dt

'''
Read in agents to create from folder.
'''
def import_agents(dir):
    return SampleAgents
    next_id = 0
    agent_list = {}
    for file in os.listdir(dir):
        try:
            next_agent = ReadInAgent(next_id, file)
            agent_list[next_id] = next_agent
            next_id += 1
        except:
            continue
    return agent_list

'''
Calculates the rewards for each player in a prisoner's dilemma.
'''
def get_rewards(choice1, choice2):
    if choice1 == choice2:
        if choice1:
            return 3, 3 # double cooperate
        else:
            return 2, 2 # double defect
    if choice1:
        return 1, 4 # player 1 is betrayed
    else:
        return 4, 1 # player 2 is betrayed

'''
Runs an iterated prisoner's dilemma between two agents for the given number of rounds.
'''
def compete(agent1, agent2, rounds):
    score1 = score2 = 0
    last_round = [None, None]

    for i in range(rounds):
        choice1 = agent1.policy(i, score1, score2, last_round)
        choice2 = agent2.policy(i, score2, score1, [last_round[1], last_round[0]])
        last_round = [choice1, choice2]
        r1, r2 = get_rewards(choice1, choice2)
        score1 += r1
        score2 += r2
    
    return score1, score2

'''
Exports competition results to a csv
'''
def export_results(results, agent_ids):
    f = open("pd_dilemma_" + str(dt.now()) + ".csv", "x")
    w = csv.DictWriter(f, agent_ids)
    w.writeheader()
    for id in agent_ids:
        row_dict = { item[1]: results[item] for item in results if item[0] == id}
        w.writerow(row_dict)
    f.close()
    return

'''
Runs the round-robin competition between all agents.
'''
def run_competition(agent_dict, rounds):
    results = {}
    agent_ids = list(agent_dict.keys())
    for i in range(len(agent_ids)):
        for j in range(i, len(agent_ids)):
            scores = compete(agent_dict[agent_ids[i]], agent_dict[agent_ids[j]], rounds)
            results[(agent_ids[i], agent_ids[j])] = scores[0]
            results[(agent_ids[j], agent_ids[i])] = scores[1]
    export_results(results, agent_ids)

def main():
    agents = import_agents("./agents/")
    rounds = 1000
    run_competition(agents, rounds)

if __name__ == "__main__":
    main()