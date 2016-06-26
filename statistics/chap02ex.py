"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2
import math

def Mode(hist):
    """
    Returns the value with the highest frequency.
    
    hist: Hist object
    
    returns: value from Hist
    """
    preg, weeks = max([(preg, weeks) for weeks, preg in hist.Items()])
    return weeks

def AllModes(hist):
    """
    Returns value-freq pairs in decreasing order of frequency.
    
    hist: Hist object
    
    returns: iterator of value-freq pairs
    """
    return sorted(hist.Items(), key=itemgetter(1), reverse=True)

def FirstWeight(live, firsts, others):
    mean_live = live.totalwgt_lb.mean()
    mean_firsts = firsts.totalwgt_lb.mean()
    mean_others = others.totalwgt_lb.mean()
    
    var_firsts = firsts.totalwgt_lb.var()
    var_others = others.totalwgt_lb.var()
    
    print('Mean')
    print('Firsts', mean_firsts)
    print('Others', mean_others)
      """
      Mean
      Firsts 7.201094430437772
      Others 7.325855614973262
      """
    
    print('Variance')
    print('Firsts', var_firsts)
    print('Others', var_others)
      """
      Variance
      Firsts 2.0180273009157768
      Others 1.9437810258964572
      """
      
    print('Diff in lbs', mean_firsts - mean_others)
    print('Diff in oz', (mean_firsts - mean_others) * 16)
      """
      Diff in lbs -0.12476118453549034
      Diff in oz -1.9961789525678455
      """
      
    print ('Diff relative to mean',
        (mean_firsts - mean_others) / mean_live * 100 )
      """
      Diff relative to mean -1.7171423678372415
      """
      
    diff = mean_firsts - mean_others
    n1, n2 = len(firsts.totalwgt_lb), len(others.totalwgt_lb)
    pooled_var = (n1 * var_firsts + n2 * var_others) / (n1 + n2)
    pooled_sd = math.sqrt(pooled_var)
    d = diff / pooled_sd
    print("Cohen's", d)
    return d
      """
      Cohen's -0.088672927072602
      """
  
def main(script):
    """Tests the functions in this module.
    
    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)
    
    # Weight Diff
    FirstWeight(live, firsts, others)
    
    # test Mode
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert(mode == 39)
    
    # test AllModes
    modes = AllModes(hist)
    assert(modes[0][1] == 4693)
    
    for value, freq in modes[:5]:
        print(value, freq)
        
    print('%s: All tests passed.' % script)
      """
      Mode of preg length 39
      39 4693
      40 1116
      38 607
      41 587
      37 455
      chap02ex.py: All tests passed.
      """
  
if __name__ == '__main__':
    main(*sys.argv)
