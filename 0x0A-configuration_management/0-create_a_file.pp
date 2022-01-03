# Resource Type: File -> creating a file using puppet with simple configurations

file { 'school':
  ensure  => 'present',
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0774',
  content => 'I love Puppet'
}