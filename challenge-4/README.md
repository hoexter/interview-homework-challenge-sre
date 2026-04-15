# Solution
```
touch the_magic_filez.txt && ./blackbox
Congrats! :)
```

# Walkthrough
## The I'm Lucky Today Way
`strings ./blackbox` and a good guess

## The Classic One
`strace -s 1024 ./blackbox` leads to

```
access("the_magic_filez.txt", F_OK)     = -1 ENOENT (No such file or directory)
fstat(1, {st_mode=S_IFCHR|0600, st_rdev=makedev(0x88, 0x9), ...}) = 0
brk(NULL)                               = 0x563943c8b000
brk(0x563943cac000)                     = 0x563943cac000
write(1, "Ooooh, what's wrong? :(", 23Ooooh, what's wrong? :() = 23
```

which hints strongly that it's looking for that file. Unclear at that point
is if it's only checking for the file existance, or if a special content would
be required. Simple test touching it reveals it's only the file that is missing.

Instead of using `strace` one could also use `bpftrace` (or attach gdb since
it even contains debug symbols).
