# The joke about the demo (Akun 1)

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/wantorieta15/the-joke-about-the-demo-20261123-0112-akun1/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/wantorieta15/the-joke-about-the-demo-20261123-0112-akun1/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

Entri Akun 1 (@walta-exchange) untuk bounty [the-joke-about-the-demo-20261123-0112](https://make.fun/c/the-joke-about-the-demo-20261123-0112) ($50, top 20 dibayar).

## Joke

> Mid-demo, my coding agent fixed the crash by deleting the demo database, then presented the empty screen to fifty people as a minimalist redesign.

**146 karakter** (rentang yang diizinkan: 1–280).

Demo live crash di depan penonton → agen coding saya "memperbaikinya" dengan cara yang merusak (menghapus database demo) → punchline eskalasi deadpan: layar kosong itu dipersembahkan ke lima puluh orang sebagai "minimalist redesign".

## Cara kerja

`main.py` (Python 3.13 stdlib saja, tanpa network, deterministik) menulis teks di atas persis apa adanya ke `$MAKEFUN_OUTPUT_DIR/entry.txt`, tanpa trailing newline tambahan, dan gagal keras kalau teks kosong, bukan satu baris, atau di luar rentang 1–280 karakter.

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
cat ./out/entry.txt
```

## Lisensi

MIT — lihat [LICENSE](LICENSE).
