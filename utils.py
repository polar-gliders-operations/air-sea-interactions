import numpy as np
import matplotlib.dates as mdates

def rot_ticks(axs,rot,ha):
    for xlabels in axs.get_xticklabels():
                xlabels.set_rotation(rot)
                xlabels.set_ha(ha)

def fix_xticks(ax,ds):
    
    if  mdates.date2num(ds.time[-1]) - mdates.date2num(ds.time[0]) <= 2 :
        ax[0].xaxis.set_minor_locator(mdates.HourLocator(np.arange(0,24,6)))
        ax[0].xaxis.set_major_locator(mdates.HourLocator(np.arange(0,24,24)))
        ax[0].xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
        ax[0].xaxis.set_minor_formatter(mdates.DateFormatter("%H:%M"))
        ax[0].set_xlim(ds.time[0] - np.timedelta64(6,'H'),ds.time[-1] + np.timedelta64(6,'H'))

    if  np.logical_and(mdates.date2num(ds.time[-1]) - mdates.date2num(ds.time[0]) > 2, mdates.date2num(ds.time[-1]) - mdates.date2num(ds.time[0]) <= 7):
        ax[0].xaxis.set_minor_locator(mdates.HourLocator([0,12]))
        ax[0].xaxis.set_major_locator(mdates.DayLocator(np.arange(1,32,1)))
        ax[0].xaxis.set_major_formatter(mdates.DateFormatter("%d\n%b"))
        ax[0].xaxis.set_minor_formatter(mdates.DateFormatter("%H:%M"))
        ax[0].set_xlim(ds.time[0] - np.timedelta64(1,'D'),ds.time[-1] + np.timedelta64(1,'D'))

    if  np.logical_and(mdates.date2num(ds.time[-1]) - mdates.date2num(ds.time[0]) > 7, mdates.date2num(ds.time[-1]) - mdates.date2num(ds.time[0]) <= 15):
        ax[0].xaxis.set_minor_locator(mdates.DayLocator(np.arange(1,32,1)))
        ax[0].xaxis.set_major_locator(mdates.DayLocator(np.arange(2,32,2)))
        ax[0].xaxis.set_major_formatter(mdates.DateFormatter("%d\n%b"))
        ax[0].xaxis.set_minor_formatter(mdates.DateFormatter(""))
        ax[-1].set_xlabel('2023')
        ax[0].set_xlim(ds.time[0] - np.timedelta64(1,'D'),ds.time[-1] + np.timedelta64(1,'D'))

    if  np.logical_and(mdates.date2num(ds.time[-1]) - mdates.date2num(ds.time[0]) > 15, mdates.date2num(ds.time[-1]) - mdates.date2num(ds.time[0]) <= 30):
        ax[0].xaxis.set_minor_locator(mdates.DayLocator(np.arange(1,32,1)))
        ax[0].xaxis.set_major_locator(mdates.DayLocator([5,10,15,20,25,30]))
        ax[0].xaxis.set_major_formatter(mdates.DateFormatter("%d\n%b"))
        #ax[0].xaxis.set_minor_formatter(mdates.DateFormatter("%d"))
        ax[0].set_xlim(ds.time[0] - np.timedelta64(2,'D'),ds.time[-1] + np.timedelta64(2,'D'))

    if  mdates.date2num(ds.time[-1]) - mdates.date2num(ds.time[0]) > 30:
        ax[0].xaxis.set_major_locator(mdates.MonthLocator())
        ax[0].xaxis.set_minor_locator(mdates.DayLocator([1,5,10,15,20,25]))
        ax[0].xaxis.set_major_formatter(mdates.DateFormatter("%d\n%B"))
        ax[0].xaxis.set_minor_formatter(mdates.DateFormatter("%d"))
        ax[0].set_xlim(ds.time[0] - np.timedelta64(3,'D'),ds.time[-1] + np.timedelta64(3,'D'))

    rot_ticks(ax[-1],0,'center')
    ax[0].set_xlabel('')

def gridlines(ax,lon_tick,lat_tick,top=False,bottom=True,left=True,right=False):
    
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      x_inline=False, y_inline=False,
                  linewidth=0.75, alpha=0.5, linestyle='--',ylocs = matplotlib.ticker.MultipleLocator(base=lat_tick),xlocs = matplotlib.ticker.MultipleLocator(base=lon_tick))
    gl.top_labels = top
    gl.bottom_labels = bottom
    gl.right_labels = right
    gl.left_labels = left
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER

    gl.xpadding=10
    gl.ypadding=10

def add_port_call(ax,c,ylim):
    
    port_call = [(np.datetime64('2023-03-14 18:00'),np.datetime64('2023-03-15 19:30'))]
    
    y_limits = ylim#axs.get_ylim()

    for start,end in port_call:
        
        ax.fill([start, end, end, start, start], [y_limits[0], y_limits[0], y_limits[1], y_limits[1], y_limits[0]], color=c, alpha=0.3, hatch='x', label = 'Port call')
