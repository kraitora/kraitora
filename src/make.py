import argparse
import os
import sys
parser = argparse.ArgumentParser()
parser.add_argument('--build-dir', default='build',
                    help='The directory of which the build was prepared.')
parser.add_argument('--panda3d-dir', default='C:/Panda3D-1.11.0-x64',
                    help='The path to the Panda3D build to use for this distribution.')
parser.add_argument('--output', default='../bin/GameData',
                    help='The built file.')
parser.add_argument('--main-module', default='toontown/toonbase/StartCompiledGame.py',
                    help='The path to the instantiation module.')
parser.add_argument('modules', nargs='*', default=['otp', 'toontown'],
                    help='The Toontown modules to be included in the build.')
args = parser.parse_args()

print ('Building the client...')
if not os.path.isdir('bin'):
    os.mkdir('bin')
os.chdir(args.build_dir)
if sys.platform == "win32":
    cmd = os.path.join(args.panda3d_dir, 'python/python.exe')
else:
    cmd = 'python3'
cmd += ' -m direct.dist.pfreeze'
cmd += ' -x panda3d'
args.modules.extend(['pandac', 'direct'])
for module in args.modules:
    cmd += ' -i {0}.*.*'.format(module)
cmd += ' -i {0}.*'.format('encodings')
cmd += ' -i {0}'.format('base64')
cmd += ' -i {0}'.format('site')
cmd += ' -i {0}'.format('_strptime')
cmd += ' -o {0}'.format(args.output)
cmd += ' {0}'.format(args.main_module)
os.system(cmd)
