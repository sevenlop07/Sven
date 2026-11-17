#!/bin/bash
# checks.sh s001:1 s007:20 ... -> caps/chk_sheet.jpg (portrait, as it will look)
cd "$(dirname "$0")"
args=""; i=0; fc=""
for pair in "$@"; do id=${pair%%:*}; fr=${pair##*:}
  printf 'shared.MT.roll = 90\nlocal ok, e = pcall(function() shared.MT.cur = nil; shared.MT.frame("%s", %s) end)\ntask.wait(1.3)\nreturn ok and "ok" or ("ERR " .. tostring(e))' "$id" "$fr" > _ck.lua
  r=$(python3 rb.py lua _ck.lua); echo "$id $r"
  python3 rb.py cap "caps/ck_$id.jpg" > /dev/null
  args="$args -i caps/ck_$id.jpg"; fc="$fc[$i:v]crop=ih*9/16:ih,scale=300:534,drawtext=text='$id':x=4:y=4:fontsize=16:fontcolor=white:box=1:boxcolor=black[v$i];"; i=$((i+1))
done
lay=""; for j in $(seq 0 $((i-1))); do lay="$lay|$(( (j%6)*300 ))_$(( (j/6)*534 ))"; done
ffmpeg -y -v error $args -filter_complex "$fc$(for j in $(seq 0 $((i-1))); do printf "[v$j]"; done)xstack=inputs=$i:layout=${lay#|}:fill=black" -q:v 4 caps/chk_sheet.jpg && echo sheet ok
