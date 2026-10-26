"""PhysGuard: Fisher-guided gradient projection for sim-to-real neural PDE surrogates.

Official implementation of the NeurIPS 2026 paper:

    Changjian Zhou, Junfeng Fang, Negin Yousefpour, Peng Wu, Bin Yan,
    Guillermo Narsilio. "PhysGuard: Fisher-Guided Gradient Projection for
    Sim-to-Real Neural PDE Surrogates." Advances in Neural Information
    Processing Systems (NeurIPS), 2026.  https://arxiv.org/abs/2606.16602
"""

__version__ = "1.0.0"
__paper__ = "https://arxiv.org/abs/2606.16602"
__venue__ = "NeurIPS 2026"

from physguard.projector import NullSpaceProjector
from physguard.optimizer import NullSpaceOptimizer

__all__ = ["NullSpaceProjector", "NullSpaceOptimizer"]
