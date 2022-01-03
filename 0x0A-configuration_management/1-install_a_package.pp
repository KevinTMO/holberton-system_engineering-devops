# Resource Type: package -> installing puppet-lint Trying: global var

$style = 'puppet-lint'

package { $style:
  ensure   => '1.1.0',
  provider => 'gem'
}