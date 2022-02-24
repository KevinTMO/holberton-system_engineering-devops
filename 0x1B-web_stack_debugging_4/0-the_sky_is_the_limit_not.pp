# Changing the limit value of request from 15 to 2000

exec { 'IncrementingVal':
  command => 'sed -i "s/15/2000/" /etc/default/nginx',
  path    => '/bin'
}

# restarting nginx web-server

exec { 'restartNginx':
  command => '/usr/sbin/service nginx restart'
}