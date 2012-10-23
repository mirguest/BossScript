#!/usr/bin/env python

import sys
import os.path

if len(sys.argv) == 2:
  try:
    import ConfigParser
    config = ConfigParser.RawConfigParser()
    config.read( os.path.expanduser('~/.bossrc') )
    config.items(sys.argv[1])
  except:
    sys.exit(-1)
elif len(sys.argv) != 3:
  sys.exit(-1)
else:
  try:
    import ConfigParser
    config = ConfigParser.RawConfigParser()
    config.read(os.path.expanduser('~/.bossrc'))
    print config.get(sys.argv[1], sys.argv[2])
  except:
    sys.exit(-1)
