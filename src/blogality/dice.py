""" A die simulation.

"""
import numpy as np


class Die:
    """
    A standard die (plural dice). By default it'll have 6 faces.
    If no randseed is provided, then the sequence of outcomes
    will not repeat for a really long time.

    Attributes:
        faces (int): The number of possible outcomes of this die.
        randseed (int): Used to ensure repeatability if desired.

    """
    def __init__(self, faces: int = 6, randseed: int = 0) -> None:
        self.randseed = randseed
        if randseed:
            self.rng = np.random.RandomState(randseed)
        else:
            self.rng = np.random.RandomState()
        self.faces = faces

    def restart(self) -> None:
        """ Reset the random number sequence.

        This will only have an effect if randseed is non-zero.

        Returns:
            None. The next call to :py:meth:`roll` will start its
            sequence from the beginning again.

        """
        if self.randseed:
            self.rng = np.random.RandomState(self.randseed)

    def roll(self) -> int:
        """ Simulate rolling this die.

        Returns:
            Int with the face that is on top after rolling this die.
            It will be a number between 1 and the number of faces, inclusive.

        """
        return self.rng.randint(1, self.faces)
