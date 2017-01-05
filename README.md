# Brace.Shell
The Ultimate Brace command interpretator!

# Sample

  #!/usr/bin/env brace.shell
  
  # Author: {Boril; Boyanov}
  
  # License: {BSD; 2 clauses}
  
  # github: 
  
  say {Hello world! [:user] please log in}
  
  password = read { Enter your password }

  require Feed.Hash { from! ./brace/stash/hash/ !! }

  pass hash = Feed.Hash.new [ password ]

  say { To be continued... Stay Psyched! More To come }
  
  # ======================================================================
  # |New-ton::
  # |? F = m * a
  # | 
  # |
  # | Newton:
  # |   force = io.mass `* a { `\* }
  # |   ???
  # |                             
  # | ! fakturiel = ([ if? ... ]; (fakturiel {n `- 1}); `$- operatoro) !!|
  # ======================================================================
