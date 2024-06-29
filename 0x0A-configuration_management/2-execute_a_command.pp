# Kill the process named killmenow
exec { 'kill_killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => '/usr/bin',
  onlyif  => '/usr/bin/pgrep  killmenow',
}
