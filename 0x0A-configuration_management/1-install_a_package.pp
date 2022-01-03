# Resource Type: package -> installing puppet-lint Trying: global var

package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem'
}