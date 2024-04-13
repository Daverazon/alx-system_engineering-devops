# Update the ssh configuration settings

augeas {'update_ssh_config':
  incl    => '/etc/ssh/ssh_config',
  lens    => 'Ssh.lns',
  changes => [
  'set Host/*/PasswordAuthentication no',
  'set Host/*/IdentifyFile ~/.ssh/school'
  ]
}
