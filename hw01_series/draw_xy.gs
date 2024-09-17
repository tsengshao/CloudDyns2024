'reinit'
vvmPath="/data/C.shaoyu/CloudDyns2024/vvm/pbl_control/gs_ctl_files"
'open 'vvmPath'/thermodynamic.ctl'
'open 'vvmPath'/dynamic.ctl'

'set lwid 15 5'
'set xlopts 1 10 0.2'
'set ylopts 1 10 0.2'

'set lev 1000'
'set gxout grfill'

'set cmark 0'
it=1
while(it<=721)
'c'
'set xlabs 0|12.8|25.6'
'set ylabs 0|12.8|25.6'

'color -1 1 0.2 -gxout grfill'
'd w.2(t='it')'
'cbar'

'set annot 1 10'
'draw ylab [km]'
'draw xlab [km]'

time=(it-1)/30+5
'draw title W[m/s] 'time':00'

'! mkdir -p fig'
'printim ./fig/w_'it'.png'

if (it=1)
it=it+30
else
it=it+180
endif
endwhile

