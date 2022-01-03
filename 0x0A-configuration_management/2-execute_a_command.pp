# Resource Type: exec -> execute a command 'pkill' to kill a process

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}