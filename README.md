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

  pass hash = Feed.Hash.New [ password ]

  say { To be continued... Stay Psyched! More To come }
  
  
  require Base.Phys.Force.Mechanical { from! ./brace/stash/physics/base/base.py !!; method! /usr/bin/env/python !! }
  
  force_1 = Base.Phys.Force.Mechanical.New {m} {a} -> m * a ! . {! No; Error Expected... Srry about this __READER__ !}

  Law_2 = force_2 -> -force_1 @ !

  Qty 1 = force_1 {3; pounds; a Three Pounder cannon} {500; m/s^2; WARNING *Slightly Better Gunpowder* }
  ... !{1 To do Smells like ... Gunpowder in the Morning Awwwyeeaaah Time for CODE meditation !}
