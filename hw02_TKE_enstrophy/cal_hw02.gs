'reinit'
*/data/C.shaoyu/CloudDyns2024/data/hw02_TKE_enstrophy/mean_series.dat

exp='pbl_control'
vvmPath='/data/C.shaoyu/CloudDyns2024/vvm/'exp'/'
gsPath=vvmPath'/gs_ctl_files/'
datPath='/data/C.shaoyu/CloudDyns2024/data/hw02/'
'! mkdir -p 'datPath

'open 'gsPath'/dynamic.ctl'
'open 'gsPath'/thermodynamic.ctl'
'open 'gsPath'/bar.ctl'

'set x 1'
'set y 1'
'set z 1 50'

'set gxout fwrite'
'set fwrite 'datPath'/domain_average.dat'

it=1
while(it<=721)
say 'it='it
'set t 'it

'define tke=amean(u*u+v*v+w*w,x=1,x=128,y=1,y=128)'
'define enstrophy=amean(xi*xi+eta*eta+zeta*zeta,x=1,x=128,y=1,y=128)'
'define thavg=amean(th.2,x=1,x=128,y=1,y=128)'
'define thsuf=thavg(z=1)'
'define pbl0p5=thsuf+0.5-thavg'
'define dz=dzt.3(t=1)'
*'define dth=cdiff(thavg,z)/50'

'd tke'
'd enstrophy'
'd thavg'
'd thsuf'
'd pbl0p5'
'd cdiff(thavg,z)/dz'

it = it+1
endwhile

'disable fwrite'
exit


******** ctl format
domain_average.ctl
'
dset ^../../data/hw02/domain_average.dat
title domain average
undef -999000000
xdef 1 linear 120.95 0.0019585
ydef 1 linear 23.458 0.00179965
zdef 50 levels 0 20 60 100 140 180 220 260
 300 340 380 420 460 500 540 580 620 660
 700 740 780 820 860 900 940 980 1020 1060
 1100 1140 1180 1220 1260 1300 1340 1380 1420 1460
 1500 1540 1580 1620 1660 1700 1740 1780 1820 1860
 1900 1940
tdef 721 linear 00Z01JAN2000 1mn
vars 6
tke         50 99 domain average TKE m2/s2
enstrophy   50 99 domain average enstrophy 1/s2
thavg       50 99 domain average theta K
thsuf       50 99 domain average theta@surface K 
pbl0p5      50 99 thsuf+0.5K minus thavg K
dthdz       50 99 cdiff(thavg,z)/dz gradient of thavg
endvars
'


