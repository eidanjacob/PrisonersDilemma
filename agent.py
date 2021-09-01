import random

'''
Informal Interface for Prisoner's Dilemma Agents
'''
class AgentInterface:
    
    def __init__(self, id):
        self.id = id
    
    def policy(self, round_number: int, self_score: int, opp_score: int, last_round: list) -> bool:
        pass

'''
Tit-For-Tat Agent Class
Cooperates on the first round and then copies opponent's move for future rounds.
'''    
class TitForTat(AgentInterface):

    def policy(self, round_number: int, self_score: int, opp_score: int, last_round: list) -> bool:
        if last_round[0] is None:
            return True
        else:
            return last_round[1]

'''
Always Cooperate Agent Class
Always cooperates.
'''
class AlwaysCooperate(AgentInterface):

    def policy(self, round_number: int, self_score: int, opp_score: int, last_round: list) -> bool:
        return True

'''
Always Defect Agent Class
Always defects.
'''
class AlwaysDefect(AgentInterface):

    def policy(self, round_number: int, self_score: int, opp_score: int, last_round: list) -> bool:
        return False

'''
Random Agent Class
Selects moves randomly.
'''
class RandomAgent(AgentInterface):

    def policy(self, round_number: int, self_score: int, opp_score: int, last_round: list) -> bool:
        return random.random() < 0.5

SampleAgents = {
    0 : TitForTat(0),
    1 : AlwaysCooperate(1),
    2 : AlwaysDefect(2),
    3 : RandomAgent(3)
}

'''
Read-In Agent
Policy read in from file during initialization.
'''
class ReadInAgent(AgentInterface):

    def __init__(self, id, file):
        self.id = id
        self.policy = eval(file.open().read())