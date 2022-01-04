# Adding lines to ssh_config using puppet

file_line { 'sudo_rule_1':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'BatchMode yes'
}

file_line { 'sudo_rule_2':
  ensure => 'present',
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school'
}