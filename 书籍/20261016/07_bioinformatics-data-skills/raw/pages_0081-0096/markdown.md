\$ fg

program1 input.txt > results.txt

![](images/page_80_image_2.jpg)

## Background Processes and Hangup Signals

There’s a slight gotcha with background processes: although they run in the background and seem disconnected from our terminal, closing our terminal window would cause these processes to be killed. Unfortunately, a lot of long-running important jobs have been accidentally killed this way.

Whenever our terminal window closes, it sends a hangup signal. Hangup signals (also know as SIGHUP) are from the era in which network connections were much less reliable. A dropped connection could prevent a user from stopping an aberrant, resourcehungry process. To address this, the hangup signal is sent to all processes started from closed terminal. Nearly all Unix commandline programs stop running as soon as they receive this signal.

So beware—running a process in the background does not guarantee that it won’t die when your terminal closes. To prevent this, we need to use the tool nohup or run it from within Tmux, two topics we’ll cover in much more detail in Chapter 4.

It’s also possible to place a process already running in the foreground into the background. To do this, we first need to suspend the process, and then use the bg command to run it in the background. Suspending a process temporarily pauses it, allowing you to put it in the background. We can suspend processes by sending a stop signal through the key combination Control-z. With our imaginary program1, we would accomplish this as follows:

```txt
$ program1 input.txt > results.txt # forgot to append ampersand
$ # enter control-z
[1]+  Stopped                 program1 input.txt > results.txt
$ bg
[1]+ program1 input.txt > results.txt
```

As with fg earlier, we could also use jobs to see the suspended process’s job ID. If we have multiple running processes, we can specify which one to move to the background with bg %&lt;num&gt; (where &lt;num&gt; is the job ID).

## Killing Processes

Occasionally we need to kill a process. It’s not uncommon for a process to demand too many of our computer’s resources or become nonresponsive, requiring that we send a special signal to kill the process. Killing a process ends it for good, and unlike suspending it with a stop signal, it’s unrecoverable. If the process is currently running in your shell, you can kill it by entering Control-C. This only works if this process is running in the foreground, so if it’s in the background you’ll have to use the fg discussed earlier.

More advanced process management (including monitoring and finding processes with top and ps, and killing them with the kill command) is out of the scope of this chapter. However, there’s a lot of information about process and resource management in this chapter’s README on GitHub.

## Exit Status: How to Programmatically Tell Whether Your Command Worked

One concern with long-running processes is that you’re probably not going to wait around to monitor them. How do you know when they complete? How do you know if they successfully finished without an error? Unix programs exit with an exit status, which indicates whether a program terminated without a problem or with an error. By Unix standards, an exit status of 0 indicates the process ran successfully, and any nonzero status indicates some sort of error has occurred (and hopefully the program prints an understandable error message, too).

![](images/page_81_image_4.jpg)

## Warning Exit Statuses

Unfortunately, whether a program returns a nonzero status when it encounters an error is up to program developers. Occasionally, programmers forget to handle errors well (and this does indeed happen in bioinformatics programs), and programs can error out and still return a zero-exit status. This is yet another reason why it’s crucial to follow The Golden Rule (i.e., don’t trust your tools) and to always check your intermediate data.

The exit status isn’t printed to the terminal, but your shell will set its value to a variable in your shell (aptly named a shell variable) named \$?. We can use the echo command to look at this variable’s value after running a command:

```txt
$ program1 input.txt > results.txt
$ echo $?
0
```

Exit statuses are incredibly useful because they allow us to programmatically chain commands together in the shell. A subsequent command in a chain is run conditionally on the last command’s exit status. The shell provides two operators that implement this: one operator that runs the subsequent command only if the first command completed successfully (&&), and one operator that runs the next command only if the first completed unsuccessfully (||). If you’re familiar with concept of short-circuit evaluation, you’ll understand that these operators are short-circuiting and and or, respectively.

It’s best to see these operators in an example. Suppose we wanted to run program1, have it write its output to file, and then have program2 read this output. To avoid the problem of program2 reading a file that’s not complete because program1 terminated with an error, we want to start program2 only after program1 returns a zero (successful) exit code. The shell operator && executes subsequent commands only if previous commands have completed with a nonzero exit status:

```batch
$ program1 input.txt > intermediate-results.txt && \program2 intermediate-results.txt > results.txt
```

Using the || operator, we can have the shell execute a command only if the previous command has failed (exited with a nonzero status). This is useful for warning messages:

```shell
$ program1 input.txt > intermediate-results.txt || \
    echo "warning: an error occurred"
```

If you want to test && and ||, there are two Unix commands that do nothing but return either exit success (true) or exit failure (false). For example, think about why the following lines are printed:

```shell
$ true
$ echo $?
0
$ false
$ echo $?
1
$ true && echo "first command was a success"
first command was a success
$ true || echo "first command was not a success"
$ false || echo "first command was not a success"
first command was not a success
$ false && echo "first command was a success"
```

Additionally, if you don’t care about the exit status and you just wish to execute two commands sequentially, you can use a single semicolon (;):

```txt
\$ false; true; false; echo "none of the previous mattered"
none of the previous mattered
```

If you’ve only known the shell as something that you interacted with through a terminal, you may start to notice that it has many elements of a full programming language. This is because it is! In fact, you can write and execute shell scripts just as you do Python scripts. Keeping your bioinformatics shell work in a commented shell script kept under version control is the best way to ensure that your work is reproducible. We will discuss shell scripts in Chapter 12.

## Command Substitution

Unix users like to have the Unix shell do work for them—this is why shell expansions like wildcards and brace expansion exist (if you need a refresher, refer back to Chapter 2). Another type of useful shell expansion is command substitution. Command substitution runs a Unix command inline and returns the output as a string that can be used in another command. This opens up a lot of useful possibilities.

A good example of when this is useful is in those early days of the New Year when we haven’t yet adjusted to using the new date. For example, five days into 2013, I shared with my collaborators a directory of new results named snp-sim-01-05-2012 (in mmdd-yyyy format). After the embarrassment subsided, the Unix solution presented itself: the date command is there to programmatically return the current date as a string. We can use this string to automatically give our directories names containing the current date. We use command substitution to run the date program and replace this command with its output (the string). This is easier to understand through a simpler example:

```shell
$ grep -c '^>' input.fasta ①
416
$ echo "There are $(grep -c '^>' input.fasta) entries in my FASTA file." ②
There are 416 entries in my FASTA file.
```

1 This command uses grep to count (the -c option stands for count) the number of lines matching the pattern. In this case, our pattern ^> matches FASTA header lines. Because each FASTA file entry has a header like “>sequence-a” that begins with “>”, this command matches each of these headers and counts the number of FASTA entries.
2 Now suppose we wanted to take the output of the grep command and insert it into another command—this is what command substitution is all about. In this case, we want echo to print a message containing how many FASTA entries there are to standard output. Using command substitution, we can calculate and return the number of FASTA entries directly into this string!

Using this command substitution approach, we can easily create dated directories using the command date +%F, where the argument +%F simply tells the date program to output the date in a particular format. date has multiple formatting options, so your European colleagues can specify a date as “19 May 2011” whereas your American colleagues can specify “May 19, 2011:”

```txt
$ mkdir results-$(date +%F)
$ ls results-2015-04-13
```

In general, the format returned by date +%F is a really good one for dated directories, because when results are sorted by name, directories in this format also sort chronologically:

<table><tr><td colspan="7">$ ls -l</td></tr><tr><td>drwxr-xr-x</td><td>2</td><td>vinceb</td><td>staff</td><td>68</td><td>Feb</td><td>3 23:23 1999-07-01</td></tr><tr><td>drwxr-xr-x</td><td>2</td><td>vinceb</td><td>staff</td><td>68</td><td>Feb</td><td>3 23:22 2000-12-19</td></tr><tr><td>drwxr-xr-x</td><td>2</td><td>vinceb</td><td>staff</td><td>68</td><td>Feb</td><td>3 23:22 2011-02-03</td></tr><tr><td>drwxr-xr-x</td><td>2</td><td>vinceb</td><td>staff</td><td>68</td><td>Feb</td><td>3 23:22 2012-02-13</td></tr><tr><td>drwxr-xr-x</td><td>2</td><td>vinceb</td><td>staff</td><td>68</td><td>Feb</td><td>3 23:23 2012-05-26</td></tr><tr><td>drwxr-xr-x</td><td>2</td><td>vinceb</td><td>staff</td><td>68</td><td>Feb</td><td>3 23:22 2012-05-27</td></tr><tr><td>drwxr-xr-x</td><td>2</td><td>vinceb</td><td>staff</td><td>68</td><td>Feb</td><td>3 23:23 2012-07-04</td></tr><tr><td>drwxr-xr-x</td><td>2</td><td>vinceb</td><td>staff</td><td>68</td><td>Feb</td><td>3 23:23 2012-07-05</td></tr></table>

The cleverness behind this is what makes this date format, known as ISO 8601, useful.

![](images/page_84_image_3.jpg)

## Storing Your Unix Tricks

In Chapter 2, we made a project directory with mkdir -p and brace expansions. If you find yourself making the same project structures a lot, it’s worthwhile to store it rather than typing it out each time. Why repeat yourself?

Early Unix users were a clever (or lazy) bunch and devised a tool for storing repeated command combinations: alias. If you’re running a clever one-liner over and over again, use add alias to add it to your \~/.bashrc (or \~/.profile if on OS X). alias simply aliases your command to a shorter name alias. For example, if you always create project directories with the same directory structure, add a line like the following:

alias mkpr="mkdir -p {data/seqs,scripts,analysis}"

For small stuff like this, there’s no point writing more complex scripts; adopt the Unix way and keep it simple. Another example is that we could alias our date +%F command to today:

alias today="date +%F"

Now, entering mkdir results-\$(today) will create a dated results directory.

A word of warning, though: do not use your aliased command in project-level shell scripts! These reside in your shell’s startup file (e.g., \~/.profile or \~/.bashrc), which is outside of your project directory. If you distribute your project directory, any shell programs that require alias definitions will not work. In computing, we say that such a practice is not portable—if it moves off your system, it breaks. Writing code to be portable, even if it’s not going to run elsewhere, will help in keeping projects reproducible.

Like all good things, Unix tricks like command substitution are best used in moderation. Once you’re a bit more familiar with these tricks, they’re very quick and easy solutions to routine annoyances. In general, however, it’s best to keep things simple and know when to reach for the quick Unix solution and when to use another tool like Python or R. We’ll discuss this in more depth in Chapters 7 and 8.

# Working with Remote Machines

Most data-processing tasks in bioinformatics require more computing power than we have on our workstations, which means we must work with large servers or computing clusters. For some bioinformatics projects, it’s likely you’ll work predominantly over a network connection with remote machines. Unsurprisingly, working with remote machines can be quite frustrating for beginners and can hobble the productivity of experienced bioinformaticians. In this chapter, we’ll learn how to make working with remote machines as effortless as possible so you can focus your time and efforts on the project itself.

## Connecting to Remote Machines with SSH

There are many ways to connect to another machine over a network, but by far the most common is through the secure shell (SSH). We use SSH because it’s encrypted (which makes it secure to send passwords, edit private files, etc.), and because it’s on every Unix system. How your server, SSH, and your user account are configured is something you or your system administrator determines; this chapter won’t cover these system administration topics. The material covered in this section should help you answer common SSH questions a sysadmin may ask (e.g., “Do you have an SSH public key?”). You’ll also learn all of the basics you’ll need as a bioinformatician to SSH into remote machines.

To initialize an SSH connection to a host (in this case, biocluster.myuniversity.edu), we use the ssh command:

\$ ssh biocluster.myuniversity.edu

Password:

Last login: Sun Aug 11 11:57:59 2013 from fisher.myisp.com

**wsobchak@biocluster.myuniversity.edu\$**

When connecting to a remote host with SSH, you’ll be prompted for your remote user account’s password.
After logging in with your password, you’re granted a shell prompt on the remote host. This allows you to execute commands on the remote host just as you’d execute them locally.

SSH also works with IP addresses—for example, you could connect to a machine with ssh 192.169.237.42. If your server uses a different port than the default (port 22), or your username on the remote machine is different from your local username, you’ll need to specify these details when connecting:

\$ ssh -p 50453 cdarwin@biocluster.myuniversity.edu

Here, we’ve specified the port with the flag -p and the username by using the syntax user@domain. If you’re unable to connect to a host, using ssh -v (-v for verbose) can help you spot the issue. You can increase the verbosity by using -vv or -vvv; see man ssh for more details.

![](images/page_87_image_6.jpg)

## Storing Your Frequent SSH Hosts

Bioinformaticians are constantly having to SSH to servers, and typing out IP addresses or long domain names can become quite tedious. It’s also burdensome to remember and type out additional details like the remote server’s port or your remote username. The developers behind SSH created a clever alternative: the SSH config file. SSH config files store details about hosts you frequently connect to. This file is easy to create, and hosts stored in this file work not only with ssh, but also with two programs we’ll learn about in Chapter 6: scp and rsync.

To create a file, just create and edit the file at \~/.ssh/config. Each entry takes the following form:

```txt
Host bio_serv
    HostName 192.168.237.42
    User cdarwin
    Port 50453
```

You won’t need to specify Port and User unless these differ from the remote host’s defaults. With this file saved, you can SSH into 192.168.236.42 using the alias ssh bio\_serv rather than typing out ssh -p 50453 cdarwin@192.169.237.42.

If you’re working with many remote machine connections in many terminal tabs, it’s sometimes useful to be make sure you’re working on the host you think you are. You can always access the hostname with the command hostname:

```txt
$ hostname
biocluster.myuniversity.edu
```

Similarly, if you maintain multiple accounts on a server (e.g., a user account for analysis and a more powerful administration account for sysadmin tasks), it can be useful to check which account you’re using. The command whoami returns your username:

```txt
\$ whoami
cdarwin
```

This is especially useful if you do occasionally log in with an administrator account with more privileges—the potential risks associated with making a mistake on an account with administrator privileges are much higher, so you should always be away when you’re on this account (and minimize this time as much as possible).

## Quick Authentication with SSH Keys

SSH requires that you type your password for the account on the remote machine. However, entering a password each time you login can get tedious, and not always safe (e.g., keyboard input could be monitored). A safer, easier alternative is to use an SSH public key. Public key cryptography is a fascinating technology, but the details are outside the scope of this book. To use SSH keys to log in into remote machines without passwords, we first need to generate a public/private key pair. We do this with the command ssh-keygen. It’s very important that you note the difference between your public and private keys: you can distribute your public key to other servers, but your private key must be kept safe and secure and never shared.

Let’s generate an SSH key pair using ssh-keygen:

```txt
\$ ssh-keygen -b 2048
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/username/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/username/.ssh/id_rsa.
Your public key has been saved in /Users/username/.ssh/id_rsa.pub.
The key fingerprint is:
e1:1e:3d:01:e1:a3:ed:2b:6b:fe:c1:8e:73:7f:1f:f0
The key's randomart image is:
+--[ RSA 2048]----+
|.o... ...          |
|   .   .   o         |
|   .       *       |
|   .       o +      |
|   .       S .       |
|   o     . E        |
|   +     .         |
|oo+..  . .       |
|+=oo... o.       |
+----------+
```

This creates a private key at \~/.ssh/id\_rsa and a public key at \~/.ssh/id\_rsa.pub. ssh keygen gives you the option to use an empty password, but it’s generally recommended that you use a real password. If you’re wondering, the random art sshkeygen creates is a way of validating your keys (there are more details about this in man ssh if you’re curious).

To use password-less authentication using SSH keys, first SSH to your remote host and log in with your password. Change directories to \~/.ssh, and append the contents of your public key file (id\_rsa.pub, not your private key!) to \~/.ssh/authorized\_keys (note that the \~ may be expanded to /home/username or /Users/username depending on the remote operating system). You can append this file by copying your public key from your local system, and pasting it to the \~/.ssh/authorized\_keys file on the remote system. Some systems have an ssh-copy-id command that automatically does this for you.

Again, be sure you’re using your public key, and not the private key. If your private key ever is accidentally distributed, this compromises the security of the machines you’ve set up key-based authentication on. The \~/.ssh/id\_rsa private key has read/ write permissions only for the creator, and these restrictive permissions should be kept this way.

After you’ve added your public key to the remote host, try logging in a few times. You’ll notice that you keep getting prompted for your SSH key’s password. If you’re scratching your head wondering how this saves time, there’s one more trick to know: ssh-agent. The ssh-agent program runs in the background on your local machine, and manages your SSH key(s). ssh-agent allows you to use your keys without entering their passwords each time—exactly what we want when we frequently connect to servers. SSH agent is usually already running on Unix-based systems, but if not, you can use eval ssh-agent to start it. Then, to tell ssh-agent about our key, we use sshadd:

\$ ssh-add

Enter passphrase for /Users/username/.ssh/id\_rsa:

Identity added: /Users/username/.ssh/id\_rsa

Now, the background ssh-agent process manages our key for us, and we won’t have to enter our password each time we connect to a remote machine. I once calculated that I connect to different machines about 16 times a day, and it takes me about two seconds to enter my password on average (accounting for typing mistakes). If we were to assume I didn’t work on weekends, this works out to about 8,320 seconds, or 2.3 hours a year of just SSH connections. After 10 years, this translates to nearly an entire day wasted on just connecting to machines. Learning these tricks may take an hour or so, but over the course of a career, this really saves time.

## Maintaining Long-Running Jobs with nohup and tmux

In Chapter 3, we briefly discussed how processes (whether running in the foreground or background) will be terminated when we close our terminal window. Processes are also terminated if we disconnect from our servers or if our network connection temporarily drops out. This behavior is intentional—your program will receive the hangup signal (referred to more technically as SIGHUP), which will in almost all cases cause your application to exit immediately. Because we’re perpetually working with remote machines in our daily bioinformatics work, we need a way to prevent hangups from stopping long-running applications. Leaving your local terminal’s connection to a remote machine open while a program runs is a fragile solution—even the most reliable networks can have short outage blips. We’ll look at two preferable solutions: nohup and Tmux. If you use a cluster, there are better ways to deal with hangups (e.g., submitting batch jobs to your cluster’s software), but these depend on your specific cluster configuration. In this case, consult your system administrator.

## nohup

nohup is simple command that executes a command and catches hangup signals sent from the terminal. Because the nohup command is catching and ignoring these hangup signals, the program you’re running won’t be interrupted. Running a command with nohup is as easy as adding nohup before your command:

```txt
\$ nohup program1 > output.txt & ①
[1] 10900 ②
```

1 We run the command with all options and arguments as we would normally, but by adding nohup this program will not be interrupted if your terminal were to close or the remote connection were to drop. Additionally, it’s a good idea to redirect standard output and standard error just as we did in Chapter 3 so you can check output later.
nohup returns the process ID number (or PID), which is how you can monitor or terminate this process if you need to (covered in “Killing Processes” on page 51). Because we lose access to this process when we run it through nohup, our only way of terminating it is by referring to it by its process ID.

## Working with Remote Machines Through Tmux

An alternative to nohup is to use a terminal multiplexer. In addition to solving the hangup problem, using a terminal multiplexer will greatly increase your productivity when working over a remote connection. We’ll use a terminal multiplexer called

Tmux, but a popular alternative is GNU Screen. Tmux and Screen have similar func tionality, but Tmux is more actively developed and has some additional nice features.

Tmux (and terminal multiplexers in general) allow you to create a session containing multiple windows, each capable of running their own processes. Tmux’s sessions are persistent, meaning that all windows and their processes can easily be restored by reattaching the session.

When run on a remote machine, Tmux allows you to maintain a persistent session that won’t be lost if your connection drops or you close your terminal window to go home (or even quit your terminal program). Rather, all of Tmux’s sessions can be reattached to whatever terminal you’re currently on—just SSH back into the remote host and reattach the Tmux session. All windows will be undisturbed and all processes still running.

## Installing and Configuring Tmux

Tmux is available through most package/port managers. On OS X, Tmux can be installed through Homebrew and on Ubuntu it’s available through apt-get. After installing Tmux, I strongly suggest you go to this chapter’s directory on GitHub and download the .tmux.conf file to your home directory. Just as your shell loads configurations from \~/.profile or \~/.bashrc, Tmux will load its configurations from \~/.tmux.conf. The minimal settings in .tmux.conf make it easier to learn Tmux by giving you a useful display bar at the bottom and changing some of Tmux’s key bindings to those that are more common among Tmux users.

## Creating, Detaching, and Attaching Tmux Sessions

Tmux allows you to have multiple sessions, and within each session have multiple windows. Each Tmux session is a separate environment. Normally, I use a session for each different project I’m working on; for example, I might have a session for maize SNP calling, one for developing a new tool, and another for writing R code to analyze some Drosophila gene expression data. Within each of these sessions, I’d have multiple windows. For example, in my maize SNP calling project, I might have three windows open: one for interacting with the shell, one with a project notebook open in my text editor, and another with a Unix manual page open. Note that all of these windows are within Tmux; your terminal program’s concept of tabs and windows is entirely different from Tmux’s. Unlike Tmux, your terminal cannot maintain persistent sessions.

Let’s create a new Tmux session. To make our examples a bit easier, we’re going to do this on our local machine. However, to manage sessions on a remote host, we’d need to start Tmux on that remote host (this is often confusing for beginners). Running Tmux on a remote host is no different; we just SSH in to our host and start Tmux there. Suppose we wanted to create a Tmux session corresponding to our earlier Maize SNP calling example:

Tmux uses subcommands; the new-session subcommand just shown creates new sessions. The -s option simply gives this session a name so it’s easier to identify later. If you’re following along and you’ve correctly placed the .tmux.conf file in your home directory, your Tmux session should look like Figure 4-1.

![](images/page_92_image_2.jpg)

<details>
<summary>text_image</summary>

bash-3.2$ echo "hello, tmux"
hello, tmux
bash-3.2$
</details>

Figure 4-1. Tmux using the provided .tmux.conf file

Tmux looks just like a normal shell prompt except for the status bar it has added at the bottom of the screen (we’ll talk more about this in a bit). When Tmux is open, we interact with Tmux through keyboard shortcuts. These shortcuts are all based on first pressing Control and a, and then adding a specific key after (releasing Control-a first). By default, Tmux uses Control-b rather than Control-a, but this is a change we’ve made in our .tmux.conf to follow the configuration preferred by most Tmux users.

The most useful feature of Tmux (and terminal multiplexers in general) is the ability to detach and reattach sessions without losing our work. Let’s see how this works in Tmux. Let’s first enter something in our blank shell so we can recognize this session later: echo "hello, tmux". To detach a session, we use Control-a, followed by d (for detach). After entering this, you should see Tmux close and be returned to your regular shell prompt.

After detaching, we can see that Tmux has kept our session alive by calling tmux with the list-sessions subcommand:

\$ tmux list-sessions

maize-snps: 1 windows (created Mon Feb 10 00:06:00 2014) [180x41]

Now, let’s reattach our session. We reattach sessions with the attach-session subcommand, but the shorter attach also works:

\$ tmux attach

Note that because we only have one session running (our maize-snps session) we don’t have to specify which session to attach. Had there been more than one session running, all session names would have been listed when we executed list-sessions and we could reattach a particular session using -t &lt;session-name&gt;. With only one Tmux session running, tmux attach is equivalent to tmux attach-session -t maize-snps.

Managing remote sessions with Tmux is no different than managing sessions locally as we did earlier. The only difference is that we create our sessions on the remote host after we connect with SSH. Closing our SSH connection (either intentionally or unintentionally due to a network drop) will cause Tmux to detach any active sessions.

## Working with Tmux Windows

Each Tmux session can also contain multiple windows. This is especially handy when working on remote machines. With Tmux’s windows, a single SSH connection to a remote host can support multiple activities in different windows. Tmux also allows you to create multiple panes within a window that allow you to split your windows into parts, but to save space I’ll let the reader learn this functionality on their own. Consult the Tmux manual page (e.g., with man tmux) or read one of the many excellent Tmux tutorials on the Web.

Like other Tmux key sequences, we create and switch windows using Control-a and then another key. To create a window, we use Control-a c, and we use Control-a n and Control-a p to go to the next and previous windows, respectively. Table 4-1 lists the most commonly used Tmux key sequences. See man tmux for a complete list, or press Control-a ? from within a Tmux session.

Table 4-1. Common Tmux key sequences

| Key sequence | Action |
| --- | --- |
| Control-a d | Detach |
| Control-a c | Create new window |
| Control-a n | Go to next window |
| Control-a p | Go to previous window |
| Control-a &amp; | Kill current window (exit in shell also works) |
| Control-a , | Rename current window |
| Control-a ? | List all key sequences |

Table 4-2. Common Tmux subcommands

| Subcommand | Action |
| --- | --- |
| tmux list-sessions | List all sessions. |
| tmux new-session -s session-name | Create a new session named “session-name”. |
| tmux attach-session -t session-name | Attach a session named “session-name”. |
| tmux attach-session -d -t session-name | Attach a session named “session-name”, detaching it first. |

If you use Emacs as your text editor, you’ll quickly notice that the key binding Control-a may get in the way. To enter a literal Control-a (as used to go to the begin ning of the line in Emacs or the Bash shell), use Control-a a.