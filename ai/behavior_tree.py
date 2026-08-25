"""
Full Behavior Tree Architecture for Complex Autonomous AI Decision Making.
Includes Selector, Sequence, Inverter, Condition, Action, and Blackboard nodes.
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict, Any, Optional


class NodeStatus(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    RUNNING = "RUNNING"


class Blackboard:
    """Shared memory context for AI Behavior Tree nodes."""

    def __init__(self):
        self._data: Dict[str, Any] = {}

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._data[key] = value

    def clear(self) -> None:
        self._data.clear()


class BehaviorNode(ABC):
    """Abstract Base Class for Behavior Tree Nodes."""

    def __init__(self, name: str = "Node"):
        self.name = name
        self.status = NodeStatus.FAILURE

    @abstractmethod
    def tick(self, blackboard: Blackboard) -> NodeStatus:
        """Execute node logic and return NodeStatus."""
        pass


class SelectorNode(BehaviorNode):
    """Composite Selector Node (OR Logic: succeeds if ANY child succeeds)."""

    def __init__(self, children: List[BehaviorNode] = None, name: str = "Selector"):
        super().__init__(name)
        self.children = children if children is not None else []

    def tick(self, blackboard: Blackboard) -> NodeStatus:
        for child in self.children:
            status = child.tick(blackboard)
            if status != NodeStatus.FAILURE:
                self.status = status
                return status
        self.status = NodeStatus.FAILURE
        return NodeStatus.FAILURE


class SequenceNode(BehaviorNode):
    """Composite Sequence Node (AND Logic: succeeds ONLY if ALL children succeed)."""

    def __init__(self, children: List[BehaviorNode] = None, name: str = "Sequence"):
        super().__init__(name)
        self.children = children if children is not None else []

    def tick(self, blackboard: Blackboard) -> NodeStatus:
        for child in self.children:
            status = child.tick(blackboard)
            if status != NodeStatus.SUCCESS:
                self.status = status
                return status
        self.status = NodeStatus.SUCCESS
        return NodeStatus.SUCCESS


class InverterNode(BehaviorNode):
    """Decorator Inverter Node (Flips SUCCESS <-> FAILURE)."""

    def __init__(self, child: BehaviorNode, name: str = "Inverter"):
        super().__init__(name)
        self.child = child

    def tick(self, blackboard: Blackboard) -> NodeStatus:
        status = self.child.tick(blackboard)
        if status == NodeStatus.SUCCESS:
            self.status = NodeStatus.FAILURE
        elif status == NodeStatus.FAILURE:
            self.status = NodeStatus.SUCCESS
        else:
            self.status = status
        return self.status


class ActionNode(BehaviorNode):
    """Leaf Action Node executing concrete AI actions."""

    def __init__(self, action_fn: Any, name: str = "Action"):
        super().__init__(name)
        self.action_fn = action_fn

    def tick(self, blackboard: Blackboard) -> NodeStatus:
        result = self.action_fn(blackboard)
        self.status = NodeStatus.SUCCESS if result else NodeStatus.FAILURE
        return self.status


class ConditionNode(BehaviorNode):
    """Leaf Condition Node evaluating boolean environment predicates."""

    def __init__(self, condition_fn: Any, name: str = "Condition"):
        super().__init__(name)
        self.condition_fn = condition_fn

    def tick(self, blackboard: Blackboard) -> NodeStatus:
        result = self.condition_fn(blackboard)
        self.status = NodeStatus.SUCCESS if result else NodeStatus.FAILURE
        return self.status
