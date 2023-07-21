import soundfile as sf
from threading import Thread, Event
import numpy as np 
import bokeh
from bokeh.plotting import figure, output_file, show
from bokeh.io import push_notebook, show, output_notebook
import IPython.display as ipd 
import time
from time import sleep


def update_audio_data(fname, blockSize): 
    isf = sf.SoundFile(fname, 'r')
    len_samples = len(isf)
    len_blocks = int(len_samples / blockSize)

    output_notebook()
    data_ = np.zeros(blockSize)
    x_ = np.arange(0, len(data_))
    p = figure(plot_height=300, plot_width=600, title='Synthesizers', y_range=(-1.0, 1.0))
    l = p.line(np.arange(0,len(data_)), data_)
    t = show(p, notebook_handle=True)

    
    k = 0
    while(1):
        t0 = time.perf_counter()
        srate = 22050.0 
        block_duration = float(blockSize) / srate 
        data_ = isf.read(blockSize, always_2d=True).astype(np.float32)  
        data_ =  data_.sum(axis=1) / 2
        l.data_source.data['y'] = data_
        l.data_source.data['x'] = x_
        push_notebook(handle=t)

        t1 = time.perf_counter()
        if blockSize > (t1 - t0):
            sleep(block_duration - (t1 - t0))
        else:
            sleep(t1 - t0)
        k = k + 1 
        if (k >= len_blocks): 
            return



def time_waveform(fname, blockSize = 1024): 

    
    audioThread_ = Thread(target=update_audio_data, args=[fname, blockSize])
    audioThread_.setDaemon(True)
    audioThread_.start()


    s = '<audio id="myaudio" src="' + fname + '" preload="auto"></audio>'
    ipd.display(ipd.HTML(s))
    s1 = "document.getElementById('myaudio').play();"
    ipd.display(ipd.Javascript(s1))
