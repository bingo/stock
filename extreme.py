import pandas as pd

def _sign(number):
  '''return sign +/- of number'''
  if number==0: return ''
  elif number>0: return '+'
  else: return '-'

def _isSignChanged(data, idx):
  '''Check whether data[idx] sign is different
     than data[idx+1]
  '''
  last_idx = len(data)-1
  next_idx = idx+1
  if next_idx > last_idx: return False
  p=_sign(data[idx])
  q=_sign(data[idx+1])
  if p==q: return False
  else: return True
  
def extremeOf(data):
  '''return a sub-series of data which holds the extreme point'''
  assert isinstance(data, pd.Series)
  diff=data.shift(1)-data
  rng=xrange(0,len(diff))
  values=[_isSignChanged(diff,idx) for idx in rng]
  return data[values]

#Test Case
if __name__ == '__main__':
  from numpy.random import randn as randn
  import matplotlib.pylab as plt
  def plot(s):
    s.plot(style='k--')
    s=pd.rolling_mean(s, 20, min_periods=1)
    s.plot()
    m=extremeOf(s)
    m.plot(style='ro')
    plt.waitforbuttonpress()
    plt.close('all')
	
  #pd.Series
  s=pd.Series(randn(100), pd.date_range('20100101', periods=100))
  plot(s)
  #pd.DataFrame['Col']
  df=pd.DataFrame(randn(100,4), index=pd.date_range('20010101', periods=100),
    columns=list('ABCD'))
  s=df['C']
  plot(s)
  #Stock market
  import matplotlib.finance as fin
  from datetime import datetime
  start=datetime(2008,1,1)
  end=datetime(2009,9,1)
  quotes=fin.quotes_historical_yahoo('AAPL', start, end, asobject=True)
  df = pd.DataFrame(quotes.close, quotes.date, columns=['close'])
  s=df['close']
  plot(s)
