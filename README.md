[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/haneulmas/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/haneulmas/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Built for the [make.fun bounty](https://make.fun/bounty/news-image-20261124).

# The World in One Day: Tuesday 24 November 2026

One image that sums up Tuesday 24 November 2026. The centre is a
newsprint globe, its continents folded like pages of paper, riding a
gold orbit ring with seven region dots. Beside the globe are the five
stories that led the day, each told in a single line. Below it, eight
more stories are drawn as cards, each a picture with a label.
Underneath, a dated ledger lists all 30 stories reported that day,
numbered 01 to 30, each cut to one fact and carrying the tag of the
outlet that reported it, with a markets strip at the foot. The globe
is the whole composition: one planet, one day. Nothing else on the
page is decoration. The stars are the only marks without a story
behind them.

## What the image shows

The five leading stories: Nvidia reinstating Jensen Huang as chief
executive 11 days after he resigned, shares jumping 33 percent;
Ukraine saying seven sea drones sank the Russian corvette Merkury at
Benghazi in Libya; the COP31 climate summit in Antalya ending with
no deal, the first such failure in 17 years; a Russian strike on a
residential building in Dymer, Kyiv region, killing 11; and settler
arson attacks on five Palestinian villages in the West Bank
overnight, condemned by France.

The eight drawn cards: a candy factory fire in Indonesia killing 24;
Wall Street surging, S and P up 4.82 percent and Nasdaq up 6.51
percent; CrowdStrike's 43 billion dollar all-stock deal to buy
Zscaler; Carlos Alcaraz winning his maiden ATP Finals title in
Turin; the UK confirmed as host of the 2035 Women's World Cup;
President Trump saying he is inclined to resume strikes on Iran
after the New Year; Gukesh defending his world chess crown against
Sindarov in Geneva; and the Lowy Institute finding the US lead over
China in Asia at its narrowest since 2018.

The ledger adds 17 more stories from the same day, from a freighter
set ablaze in the Gulf of Finland to gold rising 3.40 percent, and
every row names its source.

## How it runs

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The script copies `entry.png`, the finished 1024 by 1024 picture,
into `$MAKEFUN_OUTPUT_DIR` (or `/output` when the variable is not
set). It runs on Python 3.13, uses only the standard library,
touches no network, and refuses to run if the picture is over the
1 MiB limit.

## Determinism

The output is a byte-for-byte copy of the bundled picture, so every
run writes identical bytes. Two runs were checked by comparing
SHA-256 hashes.

## Files

- `main.py`: the copy script described above.
- `entry.png`: the finished picture.
- `README.md`: this file.
- `LICENSE`: MIT license.
