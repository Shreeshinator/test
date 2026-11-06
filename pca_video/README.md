# PCA — Principal Component Analysis from First Principles

An 11 minute 40 second Manim Community Edition film that builds PCA — from *“what is a direction of greatest variance?”* to *Cu = λu* — without ever skipping a step.

## What is in this folder

| File / folder | Deliverable |
|---|---|
| `storyboard.md` | A — time-coded scene-by-scene storyboard (visuals, on-screen maths, VO, subtitle cues) |
| `pca/` | B — the runnable Manim CE source (12 scene modules + shared `common.py`) |
| `voiceover.md` | C — the exact voiceover script, timed per scene (~1,525 words ≈ 130 wpm) |
| `pca_subtitles.srt` | D — 122 subtitle cues, ≤ 2 lines, ends exactly at 11:40 |
| `verification.md` | E — independent verification of every number and identity |
| `README.md` | F — this file: install & render instructions |
| `checklist.md` | G — final quality checklist |
| `make_srt.py`, `make_storyboard.py` | generators used to keep D and A in sync with C |
| `build.sh` | one command to render all scenes and concatenate them |
| `out/pca_full.mp4` | the final concatenated video (created by `build.sh`) |

## Requirements

- Linux (or macOS), 4+ CPU cores recommended
- Python ≥ 3.10 (developed on 3.14)
- **Manim Community Edition v0.22.1** (`-r/-q` flags verified on this version)
- FFmpeg ≥ 5
- A LaTeX distribution with `amsmath`, `amssymb`, `preview` (TeX Live: `texlive-latex-base`, `texlive-latex-recommended`, `texlive-latex-extra`, `dvisvgm` are sufficient)
- Pango + Cairo (Manim's text stack): `libpango1.0-dev libcairo2-dev pkg-config`

No external images, fonts, or video assets are used — every pixel is drawn by Manim.

## Install (Ubuntu 24.04)

```bash
sudo apt-get update
sudo apt-get install -y ffmpeg dvisvgm \
  texlive-latex-base texlive-latex-recommended texlive-latex-extra \
  texlive-fonts-recommended build-essential pkg-config python3-dev \
  libpango1.0-dev libcairo2-dev libffi-dev
pip install manim==0.22.1
```

Verify with `manim checkhealth`.

## File organisation

```
pca_video/
├── build.sh                  # render everything & concatenate
├── pca/
│   ├── __init__.py
│   ├── common.py             # shared palette, axes, dataset, helpers
│   ├── scene01_problem.py    … scene12_recap.py   (class SceneNN…)
├── storyboard.md / voiceover.md / verification.md / checklist.md
├── pca_subtitles.srt
└── media/                    # manim cache (auto-created)
```

Scenes import `from pca.common import …`, so always run Manim from the project root with `PYTHONPATH` including it (the scripts and `build.sh` already do this).

## Render a single scene (for editing)

```bash
cd pca_video
PYTHONPATH=. manim render -qh pca/scene07_projection_variance.py Scene07ProjectionVariance
```

- `-ql` 480p15 (draft), `-qm` 720p30, **`-qh` 1920×1080 60fps (deliverable)**, `-qk` 4K
- Add `--format=mp4` if you want to be explicit; output lands in `media/videos/<module>/1080p60/<Scene>.mp4`
- `-n 2,4` renders only animation numbers 2–4 of the scene (useful when retiming one step)
- `-s` saves the last frame only (fast layout check)

## Render the whole film at 1080p and concatenate

```bash
cd pca_video
./build.sh -qh
```

This renders all 12 scenes, copies them to `out/SceneNN….mp4`, and concatenates with `ffmpeg -f concat -safe 0 -c copy` (stream copy — no re-encode, no quality loss).
Final file: **`out/pca_full.mp4`** — 1920×1080, 60 fps, 11:40.
For a quick proof, use `./build.sh -ql`.

## Record the voiceover & add subtitles

1. Record 12 files, one per scene, following `voiceover.md` (room tone at both ends ≈ 0.5 s).
2. Bring each file into your editor, cut to picture, and let the scene holds absorb the difference — the animation was timed to 125–135 wpm with mathematical pauses.
3. Import `pca_subtitles.srt` as a subtitle track, or burn in with ffmpeg:

```bash
ffmpeg -i out/pca_full.mp4 -vf "subtitles=pca_subtitles.srt" -c:a copy out/pca_full_subtitled.mp4
```

4. If you re-time scenes, regenerate the SRT: adjust `SCENES`/`SCENE_LEN` in `make_srt.py` and run it (word-weighted linear placement inside each slot).

The mathematics generalises to p features unchanged — C becomes a p×p symmetric matrix, eigen-decomposition proceeds identically.

## Timing budget

| Scene | Slot | Scene | Slot |
|---|---|---|---|
| 01 The problem | 0:00–0:45 | 07 Deriving uᵀCu | 6:00–7:20 |
| 02 Centring | 0:45–1:45 | 08 Optimisation | 7:20–8:05 |
| 03 Variance | 1:45–2:35 | 09 Lagrange | 8:05–9:20 |
| 04 Covariance | 2:35–3:35 | 10 Eigenvectors | 9:20–10:15 |
| 05 Scatter matrix | 3:35–4:55 | 11 The actual answer | 10:15–10:55 |
| 06 Choosing a direction | 4:55–6:00 | 12 Recap & takeaway | 10:55–11:40 |

Total 11:40 (within the required 11–12 minutes).

## Troubleshooting

- **LaTeX errors**: ensure TeX Live packages listed above are installed; `preview.sty` comes with `texlive-latex-extra`.
- **Import error for `pca.common`**: run from the project root and set `PYTHONPATH=.`.
- **Rendering too slow**: draft with `-ql`; final with `-qh` (do not use `-k` unless you need 4K).
- **Fonts**: Text scenes use Pango's default on your system; install `fonts-dejavu` if glyphs look wrong. MathTex always uses LaTeX's Computer Modern — consistent everywhere.
- **Concatenation artefacts**: re-encode instead of stream copy with `-c:v libx264 -crf 18 -c:a aac` if your editor dislikes mixed streams (it shouldn't — all scenes share codec/fps).
