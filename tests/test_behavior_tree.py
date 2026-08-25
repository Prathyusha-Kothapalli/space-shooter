"""
Test 7: AI Behavior Tree Evaluation Logic assertions.
"""

import unittest
from ai.behavior_tree import (
    BehaviorNode, SelectorNode, SequenceNode, InverterNode,
    ActionNode, ConditionNode, Blackboard, NodeStatus
)


class TestBehaviorTree(unittest.TestCase):
    def test_sequence_node(self):
        """Verify Sequence Node requires ALL children to succeed."""
        blackboard = Blackboard()
        blackboard.set("hp", 100)

        cond1 = ConditionNode(lambda bb: bb.get("hp") > 50, "HPGreaterThan50")
        cond2 = ConditionNode(lambda bb: bb.get("hp") < 200, "HPLessThan200")
        seq = SequenceNode([cond1, cond2], "TestSeq")

        self.assertEqual(seq.tick(blackboard), NodeStatus.SUCCESS)

        # Fail sequence
        blackboard.set("hp", 10)
        self.assertEqual(seq.tick(blackboard), NodeStatus.FAILURE)

    def test_selector_node(self):
        """Verify Selector Node succeeds if ANY child succeeds."""
        blackboard = Blackboard()
        blackboard.set("mode", "EVADE")

        cond1 = ConditionNode(lambda bb: bb.get("mode") == "ATTACK", "IsAttack")
        cond2 = ConditionNode(lambda bb: bb.get("mode") == "EVADE", "IsEvade")
        sel = SelectorNode([cond1, cond2], "TestSel")

        self.assertEqual(sel.tick(blackboard), NodeStatus.SUCCESS)

    def test_inverter_node(self):
        """Verify Inverter Node flips result."""
        blackboard = Blackboard()
        cond = ConditionNode(lambda bb: True, "TrueCond")
        inv = InverterNode(cond)

        self.assertEqual(inv.tick(blackboard), NodeStatus.FAILURE)


if __name__ == "__main__":
    unittest.main()
