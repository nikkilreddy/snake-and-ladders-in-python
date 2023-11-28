"""
# Copyright Nick Cheng, Daniil Zinovyev, 2016
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

from salboard import SALboard
from salbnode import SALBnode


def salb2salbLL(salb):
    '''(SALboard)->SALBnode
    This function takes in an object which has atributes such
    as number of squares and a dictionary representing the
    snadders. After that this function creates a linked list
    representation of the board that was given and returns
    the head of it
    '''
    # This creates a variable for number of squares
    squares = salb.numSquares
    # This creates a variable for snadders
    snadders = salb.snadders
    # This creates an empty list
    node_list = []
    # This is a loop to create all nodes for each square
    for i in range(squares):
        # This puts each node for each square into a list
        node_list.append(SALBnode(next=None, snadder=None))
    # This is a counter that goes through each node
    counter = 0
    # This loops through each node in the list
    while(counter < len(node_list)):
        # This checks if the value of the square is a snadder
        if(counter + 1 in snadders):
            # If it is then that square becomes the start of the snadder
            # And is then linked to the destination of the snadder
            node_list[counter].snadder = node_list[snadders[counter + 1] - 1]
        # This checks which is the last node
        if(counter == len(node_list) - 1):
            # When the node is found then it is linked to the first
            # Node so the board is circular
            node_list[counter].next = node_list[0]
        else:
            # If the last node is not found then the loop keeps
            # Linking each square to the next one
            node_list[counter].next = node_list[counter + 1]
        # This adds 1 square each time
        counter += 1
    # This returns the head of the linked list representation of the board
    return node_list[0]


def count_squares(first_square):
    '''(SALBnode) -> int
    This function counts the number of squares there are in
    the linked list representation of the board
    >>> board = SALboard(100, {25:30, 87:65})
    >>> count_squares(salb2salbLL(board))
    100
    '''
    # This sets the number of squares
    num_squares = 1
    # This just assignes the first square to another variable
    # so it does not change
    head = first_square
    # This loops through the linked list until the moment
    # when the next square is the head square, which means
    # that it is the end of the board
    while(first_square.next != head):
        # This changes the first_square to point to the next one
        # every time it goes through a loop
        first_square = first_square.next
        # Once one loop is done number of squares in the board
        # become 1 greater
        num_squares += 1
    return num_squares


def willfinish(first, stepsize):
    '''(SALBnode, int) -> Bool
    This function takes a first node from the linked list
    representation of the board(which is the head) and
    a stepsize for a player. After that it checks if the player
    will or will not finish the game with the given stepsize
    REQ: stepsize > 0
    >>> board = SALboard(100, {25:30, 87:65})
    >>> willfinish(salb2salbLL(board), 10)
    True
    >>> board = SALboard(100, {})
    >>> willfinish(salb2salbLL(board), 7485)
    True
    >>> board = SALboard(10, {6:3})
    >>> willfinish(salb2salbLL(board), 3)
    False
    '''
    # This is the variable for a head of the linked list
    head = first
    # This sets the number of moves to 0
    num_moves = 0
    # This sets the current win condition to False
    finish = False
    # This checks the number of squares in the board
    num_squares = count_squares(first)
    # This keeps looping until the player finished the game
    # or the number of player moves exceed the number of squares
    # on the board
    while(finish is False and num_moves <= num_squares):
        # This loops as many times as the stepsize
        for i in range(stepsize):
            # This changes the first square to point to the next one
            # each time it goes through the loop
            first = first.next
        # This checks if the square that the player is on, is a snadder
        # or not
        if(first.snadder is not None):
            # If it is a snadder then make the player go to the destination
            # of the snadder
            first = first.snadder
        # This checks if the first square equals to the head, then that means
        # that the end of the board is reached
        if(first == head):
            # If the condition is true, that means that the player has reached
            # the last square and successfully completed the game
            finish = True
        # This adds one more move to the number of moves each time
        # this loop is executed
        num_moves += 1
    return finish


def whowins(first, step1, step2):
    '''
    (SALBnode, int, int) -> int
    This function takes a linked list representation of the board
    and two integers that represent the stepsizes for each player
    respectively. After that this function checks which player wins
    with the given stepsize
    REQ: stepsize > 0
    >>> board = SALboard(100, {90:60})
    >>> whowins(salb2salbLL(board), 3, 6)
    2
    >>> board = SALboard(100, {90:60})
    >>> whowins(salb2salbLL(board), 100, 6)
    1
    >>> board = SALboard(100, {90:60})
    >>> whowins(salb2salbLL(board), 10, 50)
    2
    >>> board = SALboard(100, {90:60, 57:89, 99:43})
    >>> whowins(salb2salbLL(board), 10, 50)
    2
    >>> board = SALboard(100, {90:60, 57:89, 99:43})
    >>> whowins(salb2salbLL(board), 100, 100)
    1
    '''
    # This makes the first square equal to the head, so it
    # never changes
    head = first
    # This checks the number of squares in the board
    num_squares = count_squares(first)
    # This sets the number of moves for player 1
    num_moves_player1 = 0
    # This sets the number of moves for player 2
    num_moves_player2 = 0
    # This sets the current win condition for player 1 to False
    finish1 = False
    # This sets the current win condition for player 2 to False
    finish2 = False
    # This keeps looping until the player finished the game
    # or the number of player moves exceed the number of squares
    # on the board
    while(finish1 is False and num_moves_player1 <= num_squares):
        # This loops as many times as the stepsize of player 1
        for i in range(step1):
            # This changes the first square to point to the next one
            # each time it goes through the loop
            first = first.next
        # This checks if the square that the player  1 is on, is a snadder
        # or not
        if(first.snadder is not None):
            # If it is a snadder then make the player go to the destination
            # of the snadder
            first = first.snadder
        # This checks if the first square equals to the head, then that means
        # that the end of the board is reached
        if(first == head):
            # If the condition is true, that means that the player has reached
            # the last square and successfully completed the game
            finish1 = True
        # This adds one more move to the number of moves for player 1
        # each time this loop is executed
        num_moves_player1 += 1
    # This keeps looping until the player finished the game
    # or the number of player moves exceed the number of squares
    # on the board
    while(finish2 is False and num_moves_player2 <= num_squares):
        # This loops as many times as the stepsize of player 2
        for i in range(step2):
            # This changes the first square to point to the next one
            # each time it goes through the loop
            first = first.next
        if(first.snadder is not None):
            # If it is a snadder then make the player go to the destination
            # of the snadder
            first = first.snadder
        # This checks if the first square equals to the head, then that means
        # that the end of the board is reached
        if(first == head):
            # If the condition is true, that means that the player has reached
            # the last square and successfully completed the game
            finish2 = True
        # This adds one more move to the number of moves for player 2
        # each time this loop is executed
        num_moves_player2 += 1
    # This checks if the first player has less moves and reached the
    # last square
    if(num_moves_player1 < num_moves_player2 and
       finish1 is True):
        # If the condition is met then the first player is the winner
        who_wins = 1
    # This checks if the second player has less moves and reached the
    # last square
    elif(num_moves_player1 > num_moves_player2 and
         finish2 is True):
        who_wins = 2
    # This deals with the condition when both players have finished the
    # the game and have the same number of moves
    elif(num_moves_player1 == num_moves_player2 and
         finish2 is True and finish1 is True):
        # If that is the case then player 1 is the winner
        who_wins = 1
    #  If both players stuck in the loop and never finished the game
    # then player 2 automatically wins
    else:
        who_wins = 2
    return who_wins
