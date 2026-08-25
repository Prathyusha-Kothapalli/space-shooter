"""
Boss Behavior Tree AI builder.
"""

from ai.behavior_tree import BehaviorNode, SelectorNode, SequenceNode, ConditionNode, ActionNode, Blackboard, NodeStatus


class BossBehaviorTree:
    """Constructs decision tree logic for flagship bosses."""

    @staticmethod
    def build_boss_tree(boss_entity: any) -> BehaviorNode:
        """Construct Behavior Tree for boss phase selection."""
        blackboard = Blackboard()
        blackboard.set("boss", boss_entity)

        cond_phase3 = ConditionNode(lambda bb: bb.get("boss").current_phase == 3, "IsPhase3")
        act_phase3 = ActionNode(lambda bb: True, "ExecutePhase3Attack")

        cond_phase2 = ConditionNode(lambda bb: bb.get("boss").current_phase == 2, "IsPhase2")
        act_phase2 = ActionNode(lambda bb: True, "ExecutePhase2Attack")

        act_phase1 = ActionNode(lambda bb: True, "ExecutePhase1Attack")

        seq_phase3 = SequenceNode([cond_phase3, act_phase3], "Phase3Sequence")
        seq_phase2 = SequenceNode([cond_phase2, act_phase2], "Phase2Sequence")

        root = SelectorNode([seq_phase3, seq_phase2, act_phase1], "BossRootSelector")
        return root
