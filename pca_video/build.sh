#!/bin/bash
# Build the PCA video as one concatenated 1080p file (Linux/macOS).
#
# Usage:
#   ./build.sh            # render all 12 scenes at -qh and concatenate
#   ./build.sh -ql        # quick low-res draft
set -e
QUALITY="${1:--qh}"
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
export PYTHONPATH="$ROOT${PYTHONPATH:+:$PYTHONPATH}"
mkdir -p media out

SCENES=(
  "pca/scene01_problem.py Scene01Problem"
  "pca/scene02_centering.py Scene02Centering"
  "pca/scene03_variance.py Scene03Variance"
  "pca/scene04_covariance.py Scene04Covariance"
  "pca/scene05_scatter_matrix.py Scene05ScatterMatrix"
  "pca/scene06_direction.py Scene06Direction"
  "pca/scene07_projection_variance.py Scene07ProjectionVariance"
  "pca/scene08_optimisation.py Scene08Optimisation"
  "pca/scene09_lagrange.py Scene09Lagrange"
  "pca/scene10_eigenvectors.py Scene10Eigenvectors"
  "pca/scene11_apply.py Scene11Apply"
  "pca/scene12_recap.py Scene12Recap"
)

: > out/filelist.txt
for entry in "${SCENES[@]}"; do
  set -- $entry
  file="$1"; scene="$2"
  echo "=== Rendering $scene ($QUALITY) ==="
  manim render "$QUALITY" --format=mp4 "$file" "$scene"
  # manim writes: media/videos/<module>/<quality_dir>/<SceneName>.mp4
  case "$QUALITY" in
    -ql) qdir=480p15 ;;  -qm) qdir=720p30 ;;  -qh) qdir=1080p60 ;;
    -qp) qdir=1440p60 ;; -qk) qdir=2160p60 ;;
    *)   qdir=1080p60 ;;
  esac
  mp4="media/videos/$(basename "$file" .py)/$qdir/${scene}.mp4"
  if [ ! -f "$mp4" ]; then echo "missing expected render: $mp4" >&2; exit 1; fi
  cp "$mp4" "out/${scene}.mp4"
  echo "file '${ROOT}/out/${scene}.mp4'" >> out/filelist.txt
done

echo "=== Concatenating ==="
ffmpeg -y -f concat -safe 0 -i out/filelist.txt -c copy out/pca_full.mp4
echo "Done: $ROOT/out/pca_full.mp4"
