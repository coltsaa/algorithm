# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:'EiJi'
def chessboard(board,tr,tc,dr,dc,size):
    if size <= 1:
        return
    global tile
    tile += 1
    current_tile = tile
    size //= 2
    if dr < tr + size and dc < tc + size:
        chessboard(board, tr, tc, dr, dc, size)
    else:
        board[tr + size - 1][tc + size - 1] = current_tile
        chessboard(board, tr, tc, tr + size - 1, tc + size - 1, size)
    if dr >= tr + size and dc < tc + size:
        chessboard(board, tr + size, tc, dr, dc, size)
    else:
        board[tr + size][tc + size - 1] = current_tile
        chessboard(board, tr + size, tc,
                   tr + size, tc + size - 1, size)
    if dr < tr + size and dc >= tc + size:
        chessboard(board, tr, tc + size, dr, dc, size)
    else:
        board[tr + size - 1][tc + size] = current_tile
        chessboard(board, tr, tc + size,
                   tr + size - 1, tc + size, size)
    if dr >= tr + size and dc >= tc + size:
        chessboard(board, tr + size, tc + size, dr, dc, size)
    else:
        board[tr + size][tc + size] = current_tile
        chessboard(board, tr + size, tc + size,
                   tr + size, tc + size, size)


tile = 0
size = 4
board = [[0 for x in range(size)] for y in range(size)]
chessboard(board,0,0,1,0,size)

board = [[row[i] for row in board] for i in range(len(board[0]))]
for lst in board:
    print(lst)
