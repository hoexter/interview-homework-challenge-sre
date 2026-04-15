# Solution
## Count all lines with 500 HTTP code.
```
# Quick & Dirty, could miscount if a ' 500 ' appears anywhere else:
grep -c ' 500 ' sample.log 
714

Uses the `-c` count build-in of `grep` to count matching lines.

# One could use awk to match the specific http status code field and rely only
# on that one for counting:
awk '$5=="500" {print $5}' sample.log|wc -l
714
```

Relies on `wc` to count the matching lines (`-l`) outputed by `awk`.

## Count all GET requests from yoko to /rrhh location and if it was successful (200).
```
awk '$2=="yoko" && $5=="200" && $6=="\"GET" && $7=="/rrhh\"" {print}' sample.log | wc -l
4
```

Field 2 contains the username `yoko`
Field $5 (as seen already above) the HTTP status code
Field 6 the HTTP request method and path, but since `awk` splits by space
we can still just match on that field but need to account for `"` in the
beginning.
Field 7 as the second half of the request field contains the path we can
match on.

## How many requests go to /?
```
awk '$7=="/\"" {print}' sample.log|wc -l
717
```
We leverage the same pattern from above, since the request and method in
field 6 and 7 is terminated by a `"` we can simply match on `/"` but need
to make sure to escape it.

## Count all lines without 5XX HTTP code.
```
grep -Pcv ' 5\d{2} ' sample.log 
2191
```

`-P` enables PCRE (Perl Compatible Regular Expression` so we can use `\d` to describe
digits and `{2}` to define that we want to have two of them.

`-c` for count as seen above already.

`-v` to tell group to output only lines not matching the given pattern.

## Replace all 503 HTTP codes by 500, how many requests have a 500 HTTP code?

Before the replacement we see
```
grep -c ' 500 ' sample.log 
714
```

after the 503 -> 500 replacement we see

```
sed -e 's/ 503 / 500 /' sample.log|grep -c ' 500 '
1469
```

The `sed` command matches on the ` 503 ` pattern for the status code field and replaces that one
with ` 500 `. Since `sed` prints back the complete file we need to invoke `grep -c` again to
count the new number of requests with a 500 HTTP status code.
