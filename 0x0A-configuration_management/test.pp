# Creates a file resource

file {'/root/Thinamajiga':
  ensure  => 'absent',
  mode    => '0744',
  content => 'I love King David'
}
