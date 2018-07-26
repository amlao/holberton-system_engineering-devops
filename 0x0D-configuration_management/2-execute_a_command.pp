# Using Puppet, create a manifest that kills a process named killmenow
exec { 'terminator':
  command => 'pkill killmenow'
}