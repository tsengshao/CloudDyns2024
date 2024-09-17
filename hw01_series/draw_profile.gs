'reinit'
vvmPath="/data/C.shaoyu/CloudDyns2024/vvm/pbl_control/gs_ctl_files"
'open 'vvmPath'/thermodynamic.ctl'
'open 'vvmPath'/dynamic.ctl'
'open 'vvmPath'/bar.ctl'

'set lwid 15 5'
'set xlopts 1 10 0.2'
'set ylopts 1 10 0.2'
'set xlint 3'

'set x 1'
'set y 1'
'set z 1 50'
'set t 1'

'set cthick 15'
'set cmark 0'
'set ccolor 1'

it=31
while(it<=721)
'set cmark 0'
'd th.1(t='it')'
time=(it-1)/30

pull haha
it=it+180
endwhile

'set annot 1 10'
'draw ylab [m]'
'draw xlab [K]'
'draw title theta'
*'draw title T +'it'hrs'

