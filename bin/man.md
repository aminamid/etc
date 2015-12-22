# dir_db_archive

```
$ pwd
/imail/user1/scdb/logs/db
$ /imail/user1/sleepycat/lib/dir_db_archive | head
log.0000000001
log.0000000002
$ /imail/user1/sleepycat/lib/dir_db_archive | tail
log.0000004795
log.0000004796
$ /imail/user1/sleepycat/lib/dir_db_archive -d
$ ls -la
total 3004
drwxrwx--- 2 user1 imail  159744 Dec 16 15:17 .
drwxrwx--- 4 user1 imail    4096 Nov 29 13:13 ..
-rw-rw-rw- 1 user1 imail 4194304 Dec 16 15:16 log.0000004797
$
```
