'reinit'
vvmPath="/data/C.shaoyu/CloudDyns2024/vvm/pbl_control/gs_ctl_files"
'open 'vvmPath'/surface.ctl'
'open 'vvmPath'/radiation.ctl'

'set lwid 15 5'
'set xlopts 1 10 0.2'
'set ylopts 1 10 0.2'
'set xlabs |06||08||10||12||14||16||18||20||22||24||26||28|'


'set x 1'
'set y 1'
'set t 1 last'
'set z 1 50'

'set cthick 15'
'set cmark 0'
'set ccolor 1'
'd fdsw.2(z=50)'

'set cthick 15'
'set cmark 0'
'set ccolor 2'
'd wth*1004'

'set cthick 15'
'set cmark 0'
'set ccolor 3'
'd wqv*2.5e6'

'set annot 1 10'
'draw ylab [W/m`a2`n]'
'draw xlab [hr]'
'draw title pbl_control(niterxy=300)'

pull haha

