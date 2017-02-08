# Brace.Shell
The Ultimate Brace command interpretator!

# Sample

  #!/usr/bin/env brace.shell

  # Author: {Boril; Boyanov}
  # License: {BSD; 2 clauses}
  # github:

  require {IO.Say} {from! ./base/io !!; method! << cat; unfinished >> !!}

  say = IO.Say

  say {Hello world! [:user] please log in} $

  password = read { Enter your password }

  require {Feed.Hash} { from! ./base/stash/hash/ !! }

  pass hash = Feed.Hash.New [ password ]

  say { To be continued... Stay Psyched\! More To come }


  require {Base.Phys.Force.Mechanical} { from! ./brace/stash/physics/base/base.py !!; method! /usr/bin/env/python !! }

  force_1 = Base.Phys.Force.Mechanical.New {m} {a} -> m * a ! #. {! No; Error Expected... Srry about this __READER__ !}

  Law_2 = force_2 -> -force_1 @ !

  Qty 1 = force_1 {3; pounds; a Three Pounder cannon} {500; m/s^2; WARNING *Slightly Better Gunpowder* }

  Qty 2 = say {The \:Qty 1; is [Qty 1 % 0]} {on} [Qty 1 % 1]

  IO.Say [Qty 2] $

  ...
  
