def load_env() :
 with open( '.env', 'r' ) as env :
  vars_dict = dict(
   tuple( line.replace( "\n", '' ).split( '=' ) )
   for line in env.readlines() if not line.startswith( '#' )
  )
 #for key, value in vars_dict.items() :
 # vars_dict[ key ] = value.replace( "\n", '' )
 print( vars_dict )

load_env()