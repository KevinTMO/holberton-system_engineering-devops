# Resource Type: package -> installing puppet-lint Trying: global var

$style = 'puppet-lint'

package { $style:
  ensure   => '2.5.2',
  provider => 'gem'
}