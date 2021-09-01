from agent import *
import os

'''
Read in agents to create from folder.
'''
def import_agents(dir):
    # return agent.SampleAgents
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
TODO: Export competition results to csv
'''
def export_results(results):
    return

'''
Runs the round-robin competition between all agents.
'''
def run_competition(agents, rounds):
    results = {}
    for i in range(len(agents)):
        for j in range(i, len(agents)):
            scores = compete(agents[i], agents[j], rounds)
            results[(agents[i].id, agents[j].id)] = scores[0]
            results[(agents[j].id, agents[i].id)] = scores[1]
    export_results(results)

def main():
    agents = import_agents("./agents/")
    rounds = 1000
    run_competition(agents, rounds)

if __name__ == "__main__":
    main()