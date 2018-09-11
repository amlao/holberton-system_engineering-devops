#find out why Apache is returning a 500 error
exec { 'fix_wp':
  command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -e /var/www/html/wp-settings.php'
}