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

# Do not change the declaration of SALBnode class.

class SALBnode:
    """Node for linked list representation of snakes and ladders board."""
    def __init__(self: 'SALBnode', next: 'SALBnode' = None,
                 snadder: 'SALBnode' = None) -> None:
        # Representation invariant:
        #  self.next points to the next SALBnode.
        #  If self.snadder!=None, then self is the source of a snadder
        #   whose desination is self.snadder.
        #  If self.snadder==None, then self is not the source of a snadder.
        self.next = next
        self.snadder = snadder


if __name__ == '__main__':
    import doctest
    doctest.testmod()