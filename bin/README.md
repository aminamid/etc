# filter for psps
python -c "import sys; spc=' '; exec('for l in sys.stdin:\n print spc.join(l.strip().split()[0:12])')" | column -t | sort -nk12


