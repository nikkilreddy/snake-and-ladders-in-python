"""
# Copyright Nick Cheng, 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change the declaration of SALboard class.

class SALboard:
    """Snakes And Ladders board - implemented with dictionary."""
    def __init__(self: 'SALboard', numSquares: int,
                 snadders: dict) -> None:
        # Representation invariant:
        #  numSquares is the number of squares on self.
	#  snadders is a dict of int:int.
        #  snadders[i]==j iff self has a snadder with square i as source
        #   and square j as destination.
        self.numSquares = numSquares
        self.snadders = snadders

    def __str__(self: 'SALboard') -> str:
        """Return description of SALboard self."""
        result = ('SALboard with ' + str(self.numSquares) + ' squares and ' +
                   str(len(self.snadders)) + ' snadders\n')
        for i in self.snadders:
            result = (result +  ' square ' + str(i) + ' to square ' + 
                      str(self.snadders[i]) + '\n')
        return result[:-1]

    def __eq__(self: 'SALboard', other: object) -> bool:
        """Return whether SALboard self is equivalent to other

        >>> salb1 = SALboard(100, {2: 77, 86: 5})
        >>> salb2 = SALboard(100, {86: 5, 2: 77})
        >>> salb1.__eq__(salb2)
        True
        >>> salb3 = SALboard(100,  {2: 77, 5: 86})
        >>> salb1.__eq__(salb3)
        False
        """
        return (isinstance(other, SALboard) and
                self.numSquares == other.numSquares and
                self.snadders == other.snadders)


if __name__ == '__main__':
    import doctest
    doctest.testmod()