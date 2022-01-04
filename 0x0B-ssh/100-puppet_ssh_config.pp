# Adding lines to ssh_config using puppet
include stdlib

file_line { 'rule_1':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
}

file_line { 'rule_2':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}