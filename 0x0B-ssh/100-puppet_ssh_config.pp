# Using Puppet to connect to my server without a password
file { '/etc/ssh/ssh_config':
  ensure => 'present',
}

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#PasswordAuthentication',
}

file_line { 'Use an Identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#IdentityFile',
}
