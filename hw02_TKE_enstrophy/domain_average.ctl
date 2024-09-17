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
