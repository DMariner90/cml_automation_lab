# Session 2 – Sep 16, 2025
**Topic:** WSL2 Setup & First Linux Commands  
**Milestone:** 1 – Linux & Server Fundamentals  

---

## What I Learned
- Navigating the Linux filesystem with `cd`, `pwd`, `ls`.
- Creating, copying, moving, and deleting files/directories.
- Viewing and editing file contents with `echo`, `cat`.
- Using `man` and `--help` for documentation.
- Checking system info with `whoami`, `df -h`, `free -h`.
- Changing file permissions with `chmod`.

---

## Commands Practiced
```bash
pwd                        # print working directory (where am I?)
ls -l                      # list files in long format (permissions, owner, size, date)
cd ~/notes                 # move into the notes directory
touch file1                # create an empty file
echo "Hello ENAUTO" > file1   # create file1 with text inside
cat file1                  # show file contents
cp file1 file2             # copy file1 to file2
mv file2 file3             # rename file2 → file3
rm file3                   # delete file3
mkdir practice             # create a new directory called "practice"
chmod 644 notes.txt        # set permissions: user rw, group r, others r
man ls                     # open the manual page for ls
df -h                      # show disk usage in human-readable format
free -h                    # show memory usage in human-readable format
whoami                     # display current username
uname -r                   # show kernel version


Mode	User (Owner)	Group	Others	Typical Use
600	rw-	---	---	Private file
644	rw-	r--	r--	Text files (owner can write, others read-only)
700	rwx	---	---	Private executable/script
755	rwx	r-x	r-x	Public executable/script
775	rwx	rwx	r-x	Shared directory
