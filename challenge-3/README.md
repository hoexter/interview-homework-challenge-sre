# Solution
1. Build Dockerfile with `buildah build --layers -f Dockerfile -t challenge3`
2. Start the container `podman run -p 8080:8080 -ti challenge3` (maps port 8080 to 8080 on the host and connects the terminal to the output).
3. Run `curl -H"Challenge: orcrist.org" http://lintilla:8080`, receive output `Everything works!`
