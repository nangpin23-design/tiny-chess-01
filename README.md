# tiny-chess-01 engine

A compact chess engine in a single Python file (4,095 bytes), standard library only.

## Search

- Negamax with alpha-beta pruning and iterative deepening (depths 1-7), bounded by a
  fixed global node budget (100,000 nodes per move) so play is fully deterministic -
  no clock is ever consulted.
- Quiescence search (captures and promotions only, all moves when in check) with
  delta pruning and a ply cap, so tactical sequences resolve instead of stopping
  at a bad capture.
- Move ordering: captures first (promotions first), best move from the previous
  depth tried first; root moves are re-ordered by score after each completed depth.

## Evaluation

- Incremental piece-square evaluation, maintained by make/unmake: material
  (P=100, N=320, B=330, R=500, Q=900) plus formula piece-square tables (pawn
  advance, centralisation for knights/bishops/queens, king back-rank safety).
- 0x88 board, integer pieces, incremental castling rights and en-passant tracking.

## Testing

- Correctness: perft-style checks (20 legal moves from the start position,
  castling and en-passant generation), mate-in-1 found, and incremental eval
  verified equal to full recomputation over 6 random 60-ply games (0 mismatches).
- Strength: practice trial vs the kit's house rungs (see practice/); determinism
  verified by replaying the same trial and confirming identical moves.
