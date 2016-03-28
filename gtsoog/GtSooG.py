from model import DB
from repository.RepositoryMiner import RepositoryMiner
from utils import Config
from utils import Log


def main():
    #
    cli_args = Config.parse_arguments()

    # A config file must be provided, or else nothing will work.
    if not hasattr(cli_args, 'config_file') or not cli_args.config_file:
        Log.error("A config file must be specified!")
        return
    Config.parse_config(cli_args.config_file)

    Log.info("Started. Creating database")
    DB.create_db()

    RepositoryMiner(Config.repository_path)


main()

"""
░░░░░░░░░▄░░░░░░░░░░░░░░▄
░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌    GTSOOG!
░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐
░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐     very git
░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐  much analyze
░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌
░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌     wow
░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌
░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌
▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐
▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀
"""

"""
                       P*,
                       F :9
                E.    $  :!?
                F'M:  $   :!#.,
                >':!L*"       .`P*
                L   :         .  ~M4<(*
                 r /:         '!   ! `!!<.^"*
               ,"  ~.       9: !.  !  `M !!!!  "
              F   ~'!  :    !! `! :!:  X; `~`!:4x *
              F/       /HL  !!  ~ !!!   M> \ X: M M
             F/        MM$R!.     !~   :~!  >'M:?L4M
            F~    :::  X!@!`Mk          ~`~ ' !M ! !
          .\MX:!!!!!M8X!   XRMi         '  \ ! !>' '
          .M$!!! ~!!HMRM M$RMMMM:             ~'!
          .$M!!!   -=:^~MRMMMMMM!!:            )(>
          4RM!!   @  XM$MMMMMMM!\~!:
         :$MMM!   \!~\M$RMMMMMMMX >~MH   !!..
         :MMMM!:!!!XM8$$MMMMMMMMX>` !$8x  !!!!`:!
        F$8$MMX!!!!MMMMMMMMMMMMM!> ! !$$M  !!!!.!!>
       F$$$$MMM!!!!MMMMMMMMMMMM!!~ :  !R$M  !!!X !Xh
      *@$$$$$M!!!!?!'!MM!M!XMM!!!  !   !?RM '!!M! ~M
     68$$$$$$!~~~~` !!!!!!!!!!!!~       !!?X `!MX  `
     d$$$$$$X!X!~   `!!!!!!!!!!~ :`',    !!!! `!!X
    )MMM$$$MM!XHHM$X> `!!!!!~~  :    L   `!!!! '!!!
   \MMMM$$RMMMMM$$R~          .d      r    !!!   !!.
  FXMMMMMMMMM!?M?!       uuud`         L    !!!   !!
 $:MM$MMMMMXXX!!  <    .`               b    `!>  !!
 PX!9$MMMM$$$WMMM~    @                  N    !!.  .
l ~ M$MMM$$$$$!!   .d`                    &   !!! .!
F  . M$XM$$$$R.- u`                        k   ~!!!!
  MR~ $>X$$ :> z`                           L   `!!!
k     ? @$ X:'`                              >    `!
 k ~! !:! '$R:                               `.    !
  L       !#~@                                 k   '
   `c...  z           Hoooorse                  .
                                                  k
"""
