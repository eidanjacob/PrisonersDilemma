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
Forgiving Tit-For-Tat Agent Class
Defects if last two opponent moves are both defects.
'''    
class ForgivingTitForTat(AgentInterface):

    def __init__(self, id):
        super().__init__(id)
        self.last_two_defects = 0

    def policy(self, round_number: int, self_score: int, opp_score: int, last_round: list) -> bool:
        self.last_two_defects += 1 if not last_round[1] else -1 if round_number >= 2 else 0
        if self.last_two_defects == 2:
            return False
        return True

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
    "Tit For Tat" : TitForTat("Tit for Tat"),
    "Forgiving Tit for Tat" : ForgivingTitForTat("Forgiving Tit for Tat"),
    "Always Cooperate" : AlwaysCooperate("Always Cooperate"),
    "Always Defect" : AlwaysDefect("Always Defect"),
    "Random" : RandomAgent("Random")
}