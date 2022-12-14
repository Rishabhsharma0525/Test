(*
   Parse the semgrep command line, run the requested task, and return
   an exit status.

   If called as a standalone program, the 'exit' function should be called
   with this exit status. If testing, the exit status can be checked
   against expectations.
*)
val main : string array -> Exit_code.t
