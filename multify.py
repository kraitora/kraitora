import argparse
import os

print ('Building multifiles...')
dest = os.path.join('output')
if not os.path.exists(dest):
    os.mkdir(dest)
dest = os.path.join('output/resources')
if not os.path.exists(dest):
    os.mkdir(dest)
dest = os.path.realpath(dest)
os.chdir('../resources')
for phase in os.listdir('.'):
    if not phase.startswith('phase_'):
        continue
    if not os.path.isdir(phase):
        continue
    filename = phase + '.mf'
    print ('Writing ', filename)
    filepath = os.path.join(dest, filename)
    os.system('multify -c -f "%s" "%s"' % (filepath, phase))
