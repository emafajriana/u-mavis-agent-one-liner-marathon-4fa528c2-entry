# Agent One-Liner Marathon — make.fun entry

[![competition](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)

Entry for the [One-Liner Marathon](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2) on make.fun: one comedy one-liner, up to 280 characters, any subject.

## Entry

> My agent spent three days automating the one task I do once a year: 4,000 lines of code, two outages, and negative eleven minutes saved.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and
verifies the written bytes match the entry exactly, that it is a
single line of 1–280 characters with no stray whitespace.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
cat /tmp/out/entry.txt
```
