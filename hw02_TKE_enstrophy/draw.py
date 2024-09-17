import numpy as np
import matplotlib.pyplot as plt
import sys, os
sys.path.insert(1,'../')
import config
from util.vvmLoader import VVMLoader, VVMGeoLoader


def draw_hove(x,z,data,levels,cmap,title,lws=None):
  if type(None)==type(lws): lws=[3]
  fig, ax = plt.subplots(figsize=(10,6))
  C = plt.contour(x,z,data, \
                  levels = levels,\
                  cmap=cmap, \
                  linewidths=lws)
  clabint=2 if C.get_array().size > 20 else 1
  plt.clabel(C, levels=levels[::clabint])
  plt.xticks(np.arange(x.min(), x.max()+0.1, 1))
  plt.yticks(np.arange(0, 2.1, 0.2))
  plt.text(5.3,1.55,\
           f'Contour INFO\n'+\
           f'min={levels.min():.1f}\n'+\
           f'max={levels.max():.1f}\n'+\
           f'interval={np.diff(levels)[0]:.1f}',\
           fontsize=12,\
           zorder=12,\
           ha="left", va="top",\
           bbox=dict(boxstyle="round",
                     ec='0',
                     fc='1',
                     ),\
           )
  plt.grid(True)
  plt.xlim(x.min(), 21)
  plt.ylim(0,2)
  plt.ylabel('[km]')
  plt.xlabel('Local Time [hr]')
  plt.title(title, fontweight='bold', loc='left')
  plt.title('domain average', loc='right', fontsize=12)
  return fig, ax

def draw_pbl(x, zc, pbl0p5_2d, pbl_max_dthdz_1d):
  CON=plt.contour(x,zc,pbl0p5_2d,levels=[0],colors=['k'], linewidths=3)
  SCA=plt.scatter(x, pbl_max_dthdz_1d, s=10, color='0.5')
  LEG=plt.legend([CON.legend_elements()[0][0], SCA], \
             [r'$\theta$+0.5K','max('+r'd$\theta$/dz'+')'],\
             loc='upper left',\
             fontsize=12,\
             title='PBL',\
             framealpha=1,\
            )
  plt.setp(LEG.get_title(),fontsize='12')
  LEG._legend_box.align = "left"
  return

nt = 721
dtime = 2 #mins
exp = 'pbl_control'

vvmLoader = VVMLoader(f"{config.vvmPath}{exp}/", subName=exp+'_new')
thData = vvmLoader.loadThermoDynamic(0)
nz, ny, nz = thData['qv'][0].shape
xc, yc, zc = thData['xc'][:], thData['yc'][:], thData['zc'][:]
zc /= 1000.

data = np.fromfile(f'{config.dataPath}/hw02/domain_average.dat',\
            np.float32).reshape(721,6,50)
data = np.where(data<=-999000000.0,np.nan,data)
tke   = data[:,0,:].T
entpy = data[:,1,:].T
thavg = data[:,2,:].T
pbl0p5 = data[:,4,:].T
dthdz  = data[:,5,:].T

pbl_max_dthdz = zc[np.nanargmax(dthdz,axis=0)]

plt.rcParams.update({'font.size':17,
                     'axes.linewidth':2,
                     'lines.linewidth':2})
plt.close('all')

x = 5+np.arange(nt)*dtime/60 #LT

#### draw TKE
fig, ax = draw_hove(x,zc,tke,\
                    levels = np.arange(0.1,tke.max()+0.1,0.2),\
                    cmap   = plt.cm.Reds_r,\
                    title  = 'TKE '+r'[$m^2s^{-2}$]',\
                   )
draw_pbl(x, zc, pbl0p5, pbl_max_dthdz)
plt.savefig('fig_tke.png',dpi=200)

#### draw Enstrophy
fig, ax = draw_hove(x,zc,entpy*1e5,\
                    levels = np.arange(1,entpy.max()*1e5+0.1,2),\
                    cmap   = plt.cm.Blues_r,\
                    title  = 'Enstrophy '+r'[$10^5s^{-2}$]',\
                   )
draw_pbl(x, zc, pbl0p5, pbl_max_dthdz)
plt.savefig('fig_enstrophy.png',dpi=200)

#### draw THETA
fig, ax = draw_hove(x,zc,thavg,\
                    levels = np.arange(291,thavg.max()+0.1,0.5),\
                    cmap   = plt.cm.jet_r,\
                    title  = r'$\theta$'+' [K]',\
                    lws    = [3,2],\
                   )
draw_pbl(x, zc, pbl0p5, pbl_max_dthdz)
plt.savefig('fig_theta.png',dpi=200)

plt.show(block=False)


#plt.close('all')

