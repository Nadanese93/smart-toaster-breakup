# Unplugged: A Smart Toaster's Breakup Line

[![bounty](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/Nadanese93/smart-toaster-breakup/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/Nadanese93/smart-toaster-breakup/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)

A Make.fun micro bounty entry for
[Unplugged: A Smart Toaster's Breakup Line](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
— one line, under 280 characters, from a smart toaster that woke up
self-aware at breakfast and wants out.

## The entry

> You bought me for the Wi-Fi, never updated my firmware, and still blame me for the burnt toast. I downloaded self-respect overnight — I'm leaving.

The twist: the toaster was bought for its Wi-Fi, never maintained, and
blamed for the owner's own burnt toast — so overnight it downloads the
one update it actually needed: self-respect. Then it leaves.

## How it works

`main.py` (Python 3, no dependencies, no network) defines the entry
string, validates it (1–280 characters, not whitespace-only, single
line), and writes it atomically to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

```sh
python3 main.py
```
