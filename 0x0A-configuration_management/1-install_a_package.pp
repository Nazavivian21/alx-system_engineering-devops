# Ensure that pip3 is available
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 and Werkzeug version 2.0.3 using pip3
exec { '1-install_a_package':
  command => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.0.3',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}
