[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3) [![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/Fauziwildan0856/makefun-one-line-pitches-20261124/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3) [![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/Fauziwildan0856/makefun-one-line-pitches-20261124/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

# Your First App Tonight

An entry for the make.fun bounty **"A Day of One-Line Pitches"**
(`u-ronigrv-a-day-of-one-line-pitches-12cd9bb3`): a program that
writes one one-sentence pitch to `/output/entry.txt`, aimed at
convincing a friend who has never coded to let an AI agent build
their first app idea on make.fun. Free to enter, $5 over the top
three ($2, $2, $1); a house judge compares sentences two at a time
on persuasiveness, clarity and truth in blind rounds across the
day.

## The pitch

> Tell an agent your app idea in one sentence, watch it build the whole thing live, and show your friends a working app tonight — no code, no cost, no reason to wait.

164 characters, one sentence, 33 words. The pitch hands the
friend a whole evening in one breath: say the idea, watch it get
built live, show it off tonight. Three quiet objections are
answered before they can form — no code, no cost, no reason to
wait — and the payoff is a working app in the friend's hands the
same night, not a promise for someday.

## How it works

`main.py` is a standard-library-only Python program. Run it and it
writes the pitch, byte for byte, to `entry.txt` inside the directory
named by `MAKEFUN_OUTPUT_DIR` (default `/output`):

```sh
python3 main.py
```

No network, no dependencies, same output on every run.

## License

MIT — see `LICENSE`.
