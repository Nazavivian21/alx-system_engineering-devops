#!/usr/bin/bash
#Using puppet to connect to my server without password
file {'/etc/ssh/ssh_config':
  ensure => 'present',
}
file_line {'Turn off passwd auth':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no',
    match => '^#PasswordAuthentication',
}
file_line {'Use_an_Identity_file':
    path => '/etc/ssh/ssh_config',
    line => 'IdentifyFile ~/.ssh/school',
    match => '^#IdentifyFile',
}