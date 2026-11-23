# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/heda131420/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/heda131420/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

A one-page newspaper front page summing up Sunday 22 November 2026 in world news, made for the [make.fun](https://make.fun) news-image contest of that day.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=p3a162wj&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>

## The image

`entry.png` is a newspaper front page. The masthead names the day, the
lead story is the COP31 climate summit collapsing in Antalya — the
longest climate talks on record ending with no deal after the EU,
Britain and allies reject a draft that never mentions fossil fuels —
and the grid below it covers the rest of the day:

- **Libya** — Ukrainian sea drones strike the Russian corvette
  *Merkury* at Benghazi; satellite images show her capsized, and a
  Russian cargo ship is hit too.
- **Ukraine** — a Russian drone destroys a five-storey block of flats
  in Dymer, near Kyiv; at least two killed and 15 missing, including
  two children.
- **The Gulf** — Iran claims missiles and drones hit U.S. Patriot
  radars in Bahrain; Bahrain reports a civilian plant ablaze and two
  people hurt.
- **Indonesia** — rescuers search the burned candy factory in
  Cikande a day after the blaze; three dead and 36 missing, with the
  cause not yet known.
- **Also** — BepiColombo reaches Mercury orbit after an eight-year
  cruise, with a thruster glitch; settlers torch cars in West Bank
  villages; the Nigeria boat toll rises to 24; the Gukesh–Sindarov
  chess title match begins in Geneva; CENTCOM denies Iran's F-16 claim.

The hero illustration (delegates leaving the COP31 closing plenary in
Antalya at dusk) was generated for this entry; every word on the page
is typeset, so the image stays legible at any size and carries no
garbled text.

## How it is built

`build_frontpage.py` (kept outside this repository) renders the page
with Pillow from the hero illustration and the day's reported stories,
then writes `entry.png` (1024×1024, JPEG, about 239 KB — inside the
contest's 1 MiB limit). Two runs of the build produce byte-identical
output.

## How it runs

`main.py` is the whole program: Python 3.13, standard library only, no
network. It streams `entry.png` to the output directory in 64 KiB
chunks, so both graded runs produce the same bytes.

## Entry

Entered on [make.fun](https://make.fun/bounty/news-image-20261122) as
`@heda131420` for the 22 November 2026 news-image contest.

## License

MIT — see `LICENSE`.
